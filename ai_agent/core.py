import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver  # ✅ Para async + persistence
import streamlit as st

from langchain_mcp_adapters.client import MultiServerMCPClient
from ai_agent.behavior import ATLA_BEHAVIOR

# Local Tools
from ai_agent.tools import LOCAL_TOOLS

# Load environment variables
load_dotenv()

# ✅ Função ASYNC para carregar MCP tools
async def load_mcp_tools():
    """Carrega tools MCP (GitHub)."""
    mcp_config = {
        "github": {
            "transport": "streamable_http",  # transporte HTTP suportando headers
            "url": "https://api.githubcopilot.com/mcp/",  # você usaria o endpoint público de GitHub
            "headers": {
                "Authorization": f"Bearer {st.secrets['GITHUB_ACCESS_TOKEN']}"
                }
            }
        }

    client = MultiServerMCPClient(mcp_config)
    return await client.get_tools()  # ✅ LangChain tools normais!

def get_agent_executor():
    """Configura agente com LOCAL + MCP tools."""
    
    # 1. Model
    llm = ChatOpenAI(
        model="gpt-5-nano-2025-08-07", # Modelo mais recente
        temperature=0.7,
        api_key = st.secrets["OPENAI_API_KEY"],
        streaming=True  # Para stream tokens
    )

    # 2. CARREGA MCP + MISTURA (uma única chamada async em sync func)
    mcp_tools = asyncio.run(load_mcp_tools())  # ✅ Resolve async aqui!

    # 3. ✅ TODAS as tools: LOCAL + MCP
    all_tools = LOCAL_TOOLS + mcp_tools

    # 5. ✅ Agente com MemorySaver (persiste threads)
    agent = create_agent(
        llm, 
        tools=all_tools,  # ✅ Mistura perfeita!
        system_prompt=ATLA_BEHAVIOR,
        checkpointer=MemorySaver()  # ✅ Thread persistence + async ok
    )
    
    return agent
