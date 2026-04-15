import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# ──────────────────────────────────────────────
# Load environment variables from .env file
# Works in local dev; on Render use dashboard
# env vars (no .env file needed there).
# ──────────────────────────────────────────────
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

if not OPENROUTER_API_KEY:
    raise EnvironmentError(
        "❌ OPENROUTER_API_KEY is not set. "
        "Create a .env file with: OPENROUTER_API_KEY=your-key-here"
    )

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
