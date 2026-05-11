import asyncio
import os
from typing import Any

import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver

from ai_agent.behavior import ATLAS_BEHAVIOR
from ai_agent.tools import LOCAL_TOOLS


load_dotenv()

DEFAULT_MODEL = "gpt-5-nano-2025-08-07"
GITHUB_MCP_URL = "https://api.githubcopilot.com/mcp/"


def _secret(name: str, default: str | None = None) -> str | None:
    """Read configuration from Streamlit secrets first, then environment."""
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return value or os.getenv(name, default)


def _run_async(coro: Any):
    """Run a coroutine from Streamlit's synchronous execution model."""
    return asyncio.run(coro)


async def load_mcp_tools(github_token: str | None) -> list:
    """Load GitHub MCP tools when credentials are available."""
    if not github_token:
        return []

    mcp_config = {
        "github": {
            "transport": "streamable_http",
            "url": GITHUB_MCP_URL,
            "headers": {"Authorization": f"Bearer {github_token}"},
        }
    }
    client = MultiServerMCPClient(mcp_config)
    return await client.get_tools()


def get_agent_executor():
    """Configure Atlas with local tools, optional MCP tools, and thread memory."""
    api_key = _secret("OPENAI_API_KEY")
    if not api_key:
        return None

    model = ChatOpenAI(
        model=_secret("ATLAS_MODEL", DEFAULT_MODEL),
        temperature=float(_secret("ATLAS_TEMPERATURE", "0.2")),
        api_key=api_key,
        streaming=True,
        timeout=45,
        max_retries=2,
    )

    tools = list(LOCAL_TOOLS)
    try:
        tools.extend(_run_async(load_mcp_tools(_secret("GITHUB_ACCESS_TOKEN"))))
    except Exception as exc:
        # The portfolio remains useful with local evidence tools if MCP is down.
        print(f"Atlas MCP tools unavailable: {exc}")

    return create_agent(
        model,
        tools=tools,
        system_prompt=ATLAS_BEHAVIOR,
        checkpointer=MemorySaver(),
    )
