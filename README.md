# Kendrick Bot

An AI chatbot that represents Kendrick Sin's professional profile to recruiters, hiring managers,
and collaborators. It renders inside an `<iframe>` on the
[interactive resume](https://kendricksin.github.io/interactive_resume/) and answers questions
grounded strictly in resume data — no hallucinated metrics, dates, or outcomes.

Built with FastAPI + Qwen (via DashScope), deployed on Render.

---

## How it works

```
Browser (GitHub Pages resume)
  └── <iframe src="https://kendrick-bot.onrender.com">
        └── FastAPI app (Render)
              ├── GET  /          serves the chat UI
              ├── POST /chat      streams LLM responses (SSE)
              └── GET  /health    uptime check
```

- **No database.** Conversation history is held client-side and sent with each request.
- **Streaming.** Responses appear token-by-token via Server-Sent Events.
- **Two-tier knowledge base.** Tier 1 is `resume.json` (structured facts). Tier 2 is the
  `knowledge/` files (richer context on motivations, preferences, and stories).

---

## Project structure

```
kendrick_bot/
├── main.py                  # FastAPI app — routes, rate limiting, security
├── bot.py                   # Async streaming LLM call
├── context_loader.py        # Builds system prompt from resume + knowledge files
├── resume.json              # Tier 1: structured resume data
├── knowledge/
│   ├── extended_profile.md  # Tier 2: background, motivations, working style
│   ├── job_preferences.md   # Tier 2: target roles, deal-breakers, environment
│   └── talking_points.md    # Tier 2: curated stories and achievement detail
├── static/
│   └── index.html           # Chat UI (vanilla HTML/CSS/JS)
├── requirements.txt
├── .env.example
├── render.yaml
└── .gitignore
```

---

## Running locally

### 1. Clone and install dependencies

```bash
git clone https://github.com/kendricksin/kendrick-bot.git
cd kendrick-bot
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your DashScope API key:

```
DASHSCOPE_API_KEY=sk-your-key-here
MODEL_NAME=qwen-plus
MAX_HISTORY_TURNS=10
SESSION_TURN_LIMIT=5
```

### 3. Fill in the knowledge files

Before running, populate the three placeholder files in `knowledge/`. Each file has
section headers and prompts guiding what to write:

- `knowledge/extended_profile.md` — background, motivations, working style
- `knowledge/job_preferences.md` — target roles, deal-breakers, preferred environment
- `knowledge/talking_points.md` — curated stories and key achievement detail

The bot will still work without them (it falls back to `resume.json`), but the answers
will be noticeably thinner.

### 4. Start the server

```bash
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

### Quick smoke tests

```bash
# Health check
curl http://localhost:8000/health

# Chat (non-streaming)
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"What certifications does Kendrick have?"}]}'
```

---

## Deploying on Render

### 1. Push to GitHub

```bash
git add .
git commit -m "initial commit"
git push origin main
```

Make sure `.env` is in `.gitignore` (it is by default) — never commit your API key.

### 2. Create a Render Web Service

1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo
3. Render will auto-detect `render.yaml` and pre-fill the settings:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Health check path:** `/health`

### 3. Set environment variables in Render

In the Render dashboard under **Environment**, add:

| Key | Value |
|---|---|
| `DASHSCOPE_API_KEY` | `sk-your-key-here` |
| `MODEL_NAME` | `qwen-plus` |
| `MAX_HISTORY_TURNS` | `10` |
| `SESSION_TURN_LIMIT` | `5` |

`DASHSCOPE_API_KEY` should be set as a **Secret** (Render will mask it from logs).

### 4. Deploy

Click **Deploy**. Once the build completes, your bot is live at
`https://your-service-name.onrender.com`.

### 5. Embed in the resume site

Add the iframe to your resume site:

```html
<iframe
  src="https://your-service-name.onrender.com"
  width="100%"
  height="100%"
  frameborder="0"
></iframe>
```

---

## Rate limits and session controls

| Control | Default | Env var to change |
|---|---|---|
| Requests per IP per hour | 20 | — (code only) |
| Max session turns per visitor | 5 | `SESSION_TURN_LIMIT` |
| Max input length | 500 chars | — (code only) |
| Max response tokens | 800 | — (code only) |
| Conversation history window | 10 turns | `MAX_HISTORY_TURNS` |

After 5 back-and-forth exchanges, the bot sends a session-end message and the input
is locked for that browser session. The visitor can reload the page to start a new session.

---

## Security notes

- The API key is never sent to the browser — it lives in the server environment only.
- The system prompt is injected server-side; users cannot read or override it.
- All user messages are role-whitelisted (only `user`/`assistant` roles accepted).
- Control characters and null bytes are stripped from all input.
- CORS is locked to `https://kendricksin.github.io`.
