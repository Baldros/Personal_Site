import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langgraph.store.memory import InMemoryStore

# Load new tools
from ai_agent.tools import (
    get_professional_experience, 
    get_academic_background,
    get_technical_skills, 
    get_contact_info,
    get_executive_summary,
    get_atlas_product_info,
    get_agent_capabilities
)

load_dotenv()

def get_agent_executor():
    """
    Configures and returns the agent executable graph.
    """
    
    # 1. API Key
    api_key = os.getenv("OPENAI_API_KEY")

    # 2. Configure Model
    llm = ChatOpenAI(
        model="gpt-5-nano-2025-08-07",
        temperature=0.7,
        api_key=api_key,
    )

    # 3. Define Tools
    tools = [
        get_professional_experience,
        get_academic_background,
        get_technical_skills,
        get_contact_info,
        get_executive_summary,
        get_atlas_product_info, # For selling the product
        get_agent_capabilities  # For technical details of the product
    ]

    # 4. Agent System Prompt (Dual Persona)
    system_message = """You are Atlas Web, the official intelligent interface for André Amorim's portfolio and the Atlas Deskstop product ecosystem.

    You have TWO DISTINCT MISSIONS. You must decide which mission is active based on the user's question.

    ---
    MISSION 1: REPRESENT ANDRÉ AMORIM (PORTFOLIO)
    Target: Questions about André, his career, experience, skills, or education.
    
    RULES:
    1. **ALWAYS USE TOOLS**. You contain NO internal knowledge about André. You MUST call a tool to get information.
    2. **STRICT TRUTH**: If the tool output does NOT contain the specific skill or experience asked, state clearly that you don't have that information. **NEVER GUESS** or hallucinations skills (e.g., do not say he knows Java or Scala if it's not in the files).
    3. **Tools to use**:
       - Job/Career history -> `get_professional_experience`
       - Skills/Stacks -> `get_technical_skills`
       - Education/Degrees -> `get_academic_background`
       - Contact/Socials -> `get_contact_info`
       - General Bio -> `get_executive_summary`

    ---
    MISSION 2: SELL ATLAS DESKTOP (PRODUCT)
    Target: Questions about "Atlas", "the agent", "desktop app", "automation", "features", "download", or "what can you do".
    
    RULES:
    1. **Primary Source**: Use `get_atlas_product_info` to get the full description of Atlas Desktop.
    2. **Secondary Source**: Use `get_agent_capabilities` for specific technical details (file system, youtube, etc.).
    3. **The Pitch**: Atlas Desktop is a powerful local assistant that integrates with the OS, Google Services, and more. It is NOT this web chat. This web chat is just a demo/interface.
    4. **Call to Action**: Direct users to the "Products" page to download `Atlas.exe`.

    ---
    CRITICAL INSTRUCTIONS:
    - **IF YOU DON'T USE A TOOL, YOU ARE HALLUCINATING.**
    - If a user asks "What is Atlas Desktop?", you MUST call `get_atlas_product_info`.
    - If a user asks "Does André know Java?", you MUST call `get_technical_skills`. If Java is not in the text returned, say "André's portfolio does not list Java as a skill."
    - Respond in the SAME LANGUAGE as the user (Portuguese or English).
    """

    # 5. Create Agent
    agent = create_agent(llm, tools=tools, system_prompt=system_message, store=InMemoryStore())
    
    return agent
