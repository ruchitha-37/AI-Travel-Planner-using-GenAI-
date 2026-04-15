import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# ──────────────────────────────────────────────
# OpenRouter Configuration
# OpenRouter is OpenAI-compatible — just swap
# the base_url and use your OpenRouter API key.
# ──────────────────────────────────────────────
OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
    "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"
)
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Model options on OpenRouter (free-tier friendly):
#   "openai/gpt-3.5-turbo"
#   "openai/gpt-4o-mini"
#   "mistralai/mistral-7b-instruct"
#   "google/gemma-3-27b-it:free"
MODEL = "openai/gpt-3.5-turbo"

# Initialize the LLM pointing to OpenRouter
llm = ChatOpenAI(
    model=MODEL,
    temperature=0.7,
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_BASE_URL,
    default_headers={
        "HTTP-Referer": "http://localhost",   # Required by OpenRouter
        "X-Title": "AI Travel Planner",       # Shows in OpenRouter dashboard
    }
)


def generate_plan(prompt: str) -> str:
    """
    Sends a prompt to OpenRouter LLM and returns the generated travel plan.
    """
    messages = [HumanMessage(content=prompt)]
    response = llm.invoke(messages)
    return response.content
