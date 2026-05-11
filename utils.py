import asyncio
import base64
import mimetypes
import uuid
from pathlib import Path
from typing import Any

import streamlit as st
from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage

from ai_agent.audit import export_thread_json, record_event, record_message, utc_now
from ai_agent.core import get_agent_executor


PROJECT_ROOT = Path(__file__).resolve().parent
RESOURCES_DIR = PROJECT_ROOT / "resources"
INITIAL_ASSISTANT_MESSAGE = (
    "Hello. I'm Atlas, Andre's portfolio assistant. "
    "Ask me about his experience, skills, projects, or Atlas Desktop."
)


def image_data_uri(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None

    mime_type = mimetypes.guess_type(path.name)[0] or "image/webp"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def get_featured_image_data_uri() -> str | None:
    for pattern in ("*.webp", "*.png", "*.jpg", "*.jpeg"):
        image = next(RESOURCES_DIR.glob(pattern), None)
        if image:
            return image_data_uri(image)
    return None


def load_css():
    st.markdown(
        """
    <style>
        :root {
            --atlas-bg: #f5f7fb;
            --atlas-surface: #ffffff;
            --atlas-surface-soft: #eef4f8;
            --atlas-ink: #152033;
            --atlas-muted: #5f6b7a;
            --atlas-border: #dce4ee;
            --atlas-blue: #2457a6;
            --atlas-teal: #0f8b8d;
            --atlas-green: #2f7d5a;
            --atlas-violet: #6f5aa8;
            --atlas-amber: #b46a2a;
            --atlas-shadow: 0 14px 34px rgba(17, 31, 51, 0.08);
        }

        .stApp {
            background:
                linear-gradient(180deg, rgba(255,255,255,0.86), rgba(245,247,251,0.96)),
                var(--atlas-bg);
            color: var(--atlas-ink);
            font-family: Inter, "Segoe UI", system-ui, -apple-system, sans-serif;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 1.25rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3 {
            color: var(--atlas-ink) !important;
            font-weight: 720 !important;
            letter-spacing: 0;
        }

        p, li, span, div {
            letter-spacing: 0;
        }

        a {
            color: var(--atlas-blue);
            text-decoration: none;
        }

        a:hover {
            color: var(--atlas-teal);
            text-decoration: none;
        }

        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #e8edf4;
        }

        ::-webkit-scrollbar-thumb {
            background: #9eabb9;
            border-radius: 999px;
            border: 2px solid #e8edf4;
        }

        .custom-nav {
            position: sticky;
            top: 0.65rem;
            z-index: 20;
            width: fit-content;
            max-width: 100%;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 0.25rem;
            margin: 1rem auto 2rem;
            padding: 0.35rem;
            background: rgba(255,255,255,0.86);
            border: 1px solid var(--atlas-border);
            border-radius: 999px;
            box-shadow: 0 10px 28px rgba(17,31,51,0.08);
            backdrop-filter: blur(14px);
        }

        .custom-nav a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.35rem;
            padding: 0.45rem 0.9rem;
            border-radius: 999px;
            color: #38465a;
            font-size: 0.92rem;
            font-weight: 650;
            transition: background-color 160ms ease, color 160ms ease, transform 160ms ease;
            white-space: nowrap;
        }

        .custom-nav a:hover {
            background: #e8f0fb;
            color: var(--atlas-blue);
            transform: translateY(-1px);
        }

        [data-testid="stSidebar"] {
            border-right: 1px solid var(--atlas-border);
        }

        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(180deg, #101b2e 0%, #16283f 56%, #f7f9fc 56%);
        }

        [data-testid="stSidebar"] h1 {
            color: #ffffff !important;
            font-size: 1.25rem !important;
            margin-bottom: 0.2rem;
        }

        [data-testid="stSidebar"] .stCaptionContainer {
            color: rgba(255,255,255,0.72);
        }

        [data-testid="stChatMessage"] {
            border-radius: 8px;
            border: 1px solid rgba(220,228,238,0.86);
            box-shadow: 0 8px 22px rgba(17,31,51,0.05);
        }

        .stChatFloatingInputContainer textarea {
            border-radius: 8px !important;
        }

        .stButton button,
        .stDownloadButton button {
            border-radius: 8px !important;
            border: 1px solid var(--atlas-border) !important;
            font-weight: 680 !important;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.4rem;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 8px 8px 0 0;
            font-weight: 650;
        }

        .stCard,
        .summary-card,
        .highlight-card,
        .timeline-item,
        .education-card,
        .skill-category,
        .about-intro,
        .philosophy-card,
        .link-card,
        .feature-card,
        .tech-section,
        .requirements {
            border-radius: 8px !important;
            border: 1px solid rgba(220,228,238,0.95) !important;
            box-shadow: var(--atlas-shadow) !important;
        }

        .summary-card,
        .about-intro,
        .tech-section {
            background: rgba(255,255,255,0.94) !important;
        }

        .highlight-card,
        .timeline-item,
        .education-card,
        .skill-category,
        .link-card,
        .feature-card {
            background: #ffffff !important;
            transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease !important;
        }

        .highlight-card:hover,
        .timeline-item:hover,
        .education-card:hover,
        .skill-category:hover,
        .link-card:hover,
        .feature-card:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 18px 40px rgba(17,31,51,0.11) !important;
        }

        .tech-badge,
        .skill-tag,
        .language-level {
            border-radius: 999px !important;
            letter-spacing: 0 !important;
        }

        .skill-tag.primary,
        .tech-badge,
        .download-btn {
            background: linear-gradient(135deg, var(--atlas-blue), var(--atlas-teal)) !important;
        }

        .product-hero {
            border-radius: 8px !important;
            background:
                linear-gradient(135deg, rgba(16,27,46,0.96), rgba(32,70,105,0.94)) !important;
            box-shadow: var(--atlas-shadow) !important;
        }

        .product-hero::before {
            display: none !important;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            overflow: hidden;
            border-radius: 8px;
            background: #ffffff;
            box-shadow: var(--atlas-shadow);
        }

        th {
            background: #142238;
            color: #ffffff;
            text-align: left;
            padding: 0.75rem 0.9rem;
        }

        td {
            border-top: 1px solid var(--atlas-border);
            padding: 0.7rem 0.9rem;
            color: var(--atlas-ink);
        }

        @media (max-width: 760px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .custom-nav {
                position: relative;
                top: auto;
                border-radius: 8px;
                width: 100%;
            }

            .custom-nav a {
                flex: 1 1 8rem;
            }
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def render_navbar():
    st.markdown(
        """
        <nav class="custom-nav" aria-label="Main navigation">
            <a href="." target="_self">Home</a>
            <a href="experience" target="_self">Experience</a>
            <a href="skills" target="_self">Skills</a>
            <a href="products" target="_self">Products</a>
            <a href="about" target="_self">About</a>
        </nav>
    """,
        unsafe_allow_html=True,
    )


def _initial_message() -> dict[str, Any]:
    return {
        "role": "assistant",
        "content": INITIAL_ASSISTANT_MESSAGE,
        "created_at": utc_now(),
    }


def _start_new_conversation() -> None:
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.turn_count = 0
    st.session_state.messages = [_initial_message()]
    record_event(
        st.session_state.thread_id,
        "conversation_started",
        metadata={"surface": "streamlit_sidebar"},
    )
    record_message(
        st.session_state.thread_id,
        "assistant",
        INITIAL_ASSISTANT_MESSAGE,
        turn_id=0,
        metadata={"kind": "initial_message"},
    )
    save_chat_history(st.session_state.messages, st.session_state.thread_id)


def _ensure_chat_state() -> None:
    if "app_session_id" not in st.session_state:
        st.session_state.app_session_id = str(uuid.uuid4())

    if "thread_id" not in st.session_state or "messages" not in st.session_state:
        _start_new_conversation()


@st.cache_resource(show_spinner=False)
def _cached_agent_executor():
    return get_agent_executor()


def save_chat_history(messages: list[dict[str, Any]], thread_id: str):
    return export_thread_json(thread_id, messages)


def _message_content_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
        return "".join(parts)

    return ""


def run_async_stream(agent_executor, inputs, config):
    """Bridge LangGraph async streaming into Streamlit's sync renderer."""

    async def process_stream():
        stream = agent_executor.astream(inputs, config=config, stream_mode="messages")
        async for chunk in stream:
            yield chunk

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    generator = process_stream()

    try:
        while True:
            try:
                chunk = loop.run_until_complete(generator.__anext__())
            except StopAsyncIteration:
                break

            message_chunk = chunk[0] if isinstance(chunk, tuple) else chunk
            if isinstance(message_chunk, (AIMessage, AIMessageChunk)):
                text = _message_content_to_text(message_chunk.content)
                if text:
                    yield text
    finally:
        loop.close()
        asyncio.set_event_loop(None)


def _agent_config() -> dict[str, Any]:
    thread_id = st.session_state.thread_id
    return {
        "configurable": {"thread_id": thread_id},
        "metadata": {
            "thread_id": thread_id,
            "session_id": st.session_state.app_session_id,
            "surface": "streamlit_sidebar",
        },
        "tags": ["atlas-web", "portfolio"],
    }


def render_sidebar_chat():
    """Render the Atlas chat interface in the sidebar."""
    _ensure_chat_state()

    with st.sidebar:
        st.title("Atlas")
        st.caption("Portfolio assistant")

        if st.button("New conversation", use_container_width=True):
            record_event(
                st.session_state.thread_id,
                "conversation_closed",
                metadata={"reason": "user_started_new_conversation"},
            )
            _start_new_conversation()
            st.rerun()

        agent_executor = _cached_agent_executor()
        if agent_executor:
            st.session_state.agent_executor = agent_executor
        else:
            st.warning("OPENAI_API_KEY is not configured. The chat is disabled.")

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask about Andre..."):
            turn_id = int(st.session_state.get("turn_count", 0)) + 1
            st.session_state.turn_count = turn_id

            user_message = {
                "role": "user",
                "content": prompt,
                "created_at": utc_now(),
                "turn_id": turn_id,
            }
            st.session_state.messages.append(user_message)
            record_message(st.session_state.thread_id, "user", prompt, turn_id=turn_id)
            save_chat_history(st.session_state.messages, st.session_state.thread_id)

            with st.chat_message("user"):
                st.markdown(prompt)

            if "agent_executor" not in st.session_state:
                st.error("Please configure OPENAI_API_KEY in .env or Streamlit secrets.")
                return

            with st.chat_message("assistant"):
                try:
                    with st.spinner("Atlas is checking the evidence..."):
                        response_stream = run_async_stream(
                            st.session_state.agent_executor,
                            {"messages": [HumanMessage(content=prompt)]},
                            _agent_config(),
                        )
                        final_response = st.write_stream(response_stream)

                    assistant_message = {
                        "role": "assistant",
                        "content": final_response,
                        "created_at": utc_now(),
                        "turn_id": turn_id,
                    }
                    st.session_state.messages.append(assistant_message)
                    record_message(
                        st.session_state.thread_id,
                        "assistant",
                        final_response,
                        turn_id=turn_id,
                    )
                    save_chat_history(st.session_state.messages, st.session_state.thread_id)

                except Exception as exc:
                    record_event(
                        st.session_state.thread_id,
                        "error",
                        content=str(exc),
                        turn_id=turn_id,
                        metadata={"stage": "agent_stream"},
                    )
                    st.error(f"Error processing the message: {exc}")


def setup_page(title, icon):
    st.set_page_config(page_title=f"{title} | Andre Amorim", page_icon=icon, layout="wide")
    load_css()
    render_navbar()
    render_sidebar_chat()


def card(title, content, date=None, image=None):
    with st.container():
        st.markdown(
            f"""
        <div class="stCard">
            <h3>{title}</h3>
            {f'<p style="color: #667085; font-size: 0.9rem;">{date}</p>' if date else ''}
            <p>{content}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
