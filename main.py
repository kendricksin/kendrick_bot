import json
import os
import re
from typing import AsyncGenerator

from dotenv import load_dotenv

# Load .env before any local imports so env vars are available at module init time
load_dotenv()

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from bot import stream_chat
from context_loader import build_system_prompt

# ---------------------------------------------------------------------------
# Rate limiter
# ---------------------------------------------------------------------------
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Kendrick Bot", docs_url=None, redoc_url=None)
app.state.limiter = limiter

MAX_HISTORY_TURNS = int(os.getenv("MAX_HISTORY_TURNS", 10))
SESSION_TURN_LIMIT = int(os.getenv("SESSION_TURN_LIMIT", 5))
# Rough token budget: reject if estimated prompt tokens exceed this threshold.
# Protects against expensive requests even within the turn window.
MAX_ESTIMATED_PROMPT_TOKENS = 3000

# ---------------------------------------------------------------------------
# System prompt — loaded once at startup
# ---------------------------------------------------------------------------
SYSTEM_PROMPT: str = ""


@app.on_event("startup")
async def startup_event() -> None:
    global SYSTEM_PROMPT
    SYSTEM_PROMPT = build_system_prompt()


# ---------------------------------------------------------------------------
# Exception handlers
# ---------------------------------------------------------------------------
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded. Please wait before sending more messages."
        },
    )


# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kendricksin.github.io"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_iframe_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "ALLOWALL"
    response.headers["Content-Security-Policy"] = "frame-ancestors *"
    return response


# ---------------------------------------------------------------------------
# Request model
# ---------------------------------------------------------------------------
_CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
MAX_INPUT_CHARS = 500
MAX_RAW_CONTENT_CHARS = 4000  # Pydantic hard cap before server-side checks


class Message(BaseModel):
    role: str
    content: str = Field(..., max_length=MAX_RAW_CONTENT_CHARS)


class ChatRequest(BaseModel):
    messages: list[Message] = Field(..., min_length=1)


# ---------------------------------------------------------------------------
# Session limit stream
# ---------------------------------------------------------------------------
async def _session_limit_stream() -> AsyncGenerator[str, None]:
    msg = (
        "I've answered 5 questions this session — that's my limit for now. "
        "Feel free to come back later, or reach out to Kendrick directly via "
        "[LinkedIn](https://www.linkedin.com/in/kendrick-sin-8b1b91176/) "
        "or [email](mailto:kendricksin@outlook.sg)."
    )
    yield f"data: {json.dumps({'token': msg})}\n\n"
    yield f"data: {json.dumps({'session_limit': True})}\n\n"
    yield "data: [DONE]\n\n"


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def serve_ui() -> HTMLResponse:
    ui_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    with open(ui_path, encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
@limiter.limit("20/hour")
async def chat(request: Request, body: ChatRequest) -> StreamingResponse:
    # 1. Whitelist roles — silently drop anything that isn't user/assistant
    sanitized = [
        msg for msg in body.messages if msg.role in ("user", "assistant")
    ]

    # 2. Must end with a user message
    if not sanitized or sanitized[-1].role != "user":
        raise HTTPException(status_code=400, detail="Last message must be from user.")

    # 3. Strip control characters from all messages
    cleaned: list[dict] = []
    for msg in sanitized:
        content = _CONTROL_CHAR_RE.sub("", msg.content)
        cleaned.append({"role": msg.role, "content": content})

    # 4. Enforce 500-char limit on the final user message (server-side truth)
    if len(cleaned[-1]["content"]) > MAX_INPUT_CHARS:
        raise HTTPException(
            status_code=400,
            detail=f"Message too long. Maximum {MAX_INPUT_CHARS} characters.",
        )

    # 5. Sliding window — keep last N turns (each turn = 1 user + 1 assistant)
    max_messages = MAX_HISTORY_TURNS * 2
    if len(cleaned) > max_messages:
        cleaned = cleaned[-max_messages:]

    # 5b. Session turn limit — count user messages across the whole session
    user_turn_count = sum(1 for m in cleaned if m["role"] == "user")
    if user_turn_count > SESSION_TURN_LIMIT:
        return StreamingResponse(
            _session_limit_stream(),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    # 6. Rough token budget guard — char / 4 ≈ tokens
    estimated_tokens = sum(len(m["content"]) for m in cleaned) // 4
    if estimated_tokens > MAX_ESTIMATED_PROMPT_TOKENS:
        raise HTTPException(
            status_code=400,
            detail="Conversation too long. Please start a new chat.",
        )

    return StreamingResponse(
        stream_chat(SYSTEM_PROMPT, cleaned),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
