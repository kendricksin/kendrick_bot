import json
import logging
import os
from typing import AsyncGenerator

from openai import AsyncOpenAI

logger = logging.getLogger(__name__)

_client: AsyncOpenAI | None = None


def _get_client() -> AsyncOpenAI:
    global _client
    if _client is None:
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            raise RuntimeError("DASHSCOPE_API_KEY environment variable is not set.")
        _client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
        )
    return _client


async def stream_chat(
    system_prompt: str, messages: list[dict]
) -> AsyncGenerator[str, None]:
    full_messages = [{"role": "system", "content": system_prompt}] + messages
    model = os.getenv("MODEL_NAME", "qwen-plus")
    try:
        stream = await _get_client().chat.completions.create(
            model=model,
            messages=full_messages,
            temperature=0.5,
            max_tokens=800,
            stream=True,
            extra_body={"enable_thinking": False},
        )
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                delta = chunk.choices[0].delta.content
                yield f"data: {json.dumps({'token': delta})}\n\n"
    except Exception as e:
        logger.exception("LLM call failed: %s", e)
        yield f"data: {json.dumps({'error': 'Something went wrong. Please try again.'})}\n\n"
    finally:
        yield "data: [DONE]\n\n"
