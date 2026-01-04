import streamlit as st 

def load_css():
    st.markdown("""
    <style>
        /* Global Styles */
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9fafb;
            color: #333;
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 5px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        /* Card Style */
        .stCard {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        .stCard:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
        }

        /* Headings */
        h1, h2, h3 {
            color: #0055a5;
            font-weight: 600;
        }
        
        /* Links */
        a {
            color: #0055a5;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        
        /* Sidebar */
        /* Sidebar */
        /* Sidebar is now enabled for the chat */
        
        /* Custom Navbar */
        .custom-nav {
            background: #ffffff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-radius: 50px;
            padding: 10px 30px;
            margin: 20px auto;
            width: fit-content;
            display: flex;
            gap: 20px;
            justify-content: center;
            align-items: center;
            border: 1px solid #eaeaea;
        }
        .custom-nav a {
            text-decoration: none;
            color: #555;
            font-weight: 500;
            padding: 8px 16px;
            border-radius: 20px;
            transition: all 0.3s ease;
            font-size: 0.95rem;
        }
        .custom-nav a:hover {
            background-color: #f0f7ff;
            color: #0055a5;
            transform: translateY(-1px);
        }
    </style>
    """, unsafe_allow_html=True)

def render_navbar():
    """
    Renders a custom navigation bar.
    """
    st.markdown("""
        <div class="custom-nav">
            <a href="." target="_self">Home</a>
            <a href="experience" target="_self">Experience</a>
            <a href="skills" target="_self">Skills</a>
            <a href="products" target="_self">Products</a>
            <a href="about" target="_self">About</a>
        </div>
    """, unsafe_allow_html=True)

import json
import uuid
import datetime
import os
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from ai_agent.core import get_agent_executor

def save_chat_history(messages, thread_id):
    """Saves chat history to a JSON file."""
    history_dir = "PersonalSite/History"
    if not os.path.exists(history_dir):
        os.makedirs(history_dir)
    
    filename = f"{history_dir}/chat_{thread_id}.json"
    
    # Convert messages to serializable format
    serializable_messages = []
    for msg in messages:
        serializable_messages.append({
            "role": msg["role"],
            "content": msg["content"],
            "timestamp": datetime.datetime.now().isoformat()
        })
        
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(serializable_messages, f, ensure_ascii=False, indent=4)

import asyncio

def run_async_stream(agent_executor, inputs, config):
    """
    Bridge function to run async streaming in a synchronous Streamlit app.
    It manages a new event loop to consume the async generator.
    """
    async def process_stream():
        # Setup generator
        stream = agent_executor.astream(inputs, config=config, stream_mode="messages")
        try:
             async for chunk in stream:
                 yield chunk
        except Exception as e:
            # Propagate exception
            raise e

    # Create a new loop for this sync call
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    gen = process_stream()
    
    try:
        while True:
            # Run one step of the generator
            try:
                # Get next chunk
                chunk = loop.run_until_complete(gen.__anext__())
                
                # Filter logic (same as before)
                if isinstance(chunk, tuple):
                    message_chunk, _ = chunk
                else:
                    message_chunk = chunk
                
                if isinstance(message_chunk, AIMessage) and message_chunk.content:
                    yield message_chunk.content
                    
            except StopAsyncIteration:
                break
    finally:
        loop.close()

def render_sidebar_chat():
    """
    Renders the sidebar chat interface powered by an AI Agent.
    """
    with st.sidebar:
        st.title("💬 Atlas")
        
        ## 1. User Name and Thread Initialization
        #if "user_name" not in st.session_state:
        #    with st.form("user_name_form"):
        #        name_input = st.text_input("Enter your name...", placeholder="to start to talk with my AI.")
        #        submitted = st.form_submit_button("Start Chat")
        #        if submitted and name_input:
        #            st.session_state.user_name = name_input
        #            st.rerun()
        #    return  # Stop rendering until name is provided
        
        #st.success(f"Welcome, {st.session_state.user_name}!")
        st.session_state.thread_id = str(uuid.uuid4())
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": f"Hello! I'm Atlas, André's virtual assistant. 🌎\nI'm here to answer questions about his career, skills, and projects.\nWhat would you like to know?"}
            ]
        
        # Initialize Agent Executor in session state
        if "agent_executor" not in st.session_state:
            agent_executor = get_agent_executor()
            if agent_executor:
                 st.session_state.agent_executor = agent_executor
            else:
                st.warning("⚠️ API Key not detected. Chat will not function correctly.")

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        if prompt := st.chat_input("Ask something about André..."):
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Save history immediately after user input
            save_chat_history(st.session_state.messages, st.session_state.thread_id)

            if "agent_executor" in st.session_state:
                with st.chat_message("assistant"):
                    try:
                        # Prepare JUST the new messages for LangGraph
                        # (MemorySaver handles the history persistence)
                        input_messages = []
                        
                        # Inject User Name Context (as a reminder/system instruction)
                        # We use SystemMessage to treat it as instruction, not conversation history
                        #input_messages.append(SystemMessage(content=f"The user's name is {st.session_state.user_name}. Always address them by name when appropriate."))
                        
                        # Add ONLY the latest user prompt
                        input_messages.append(HumanMessage(content=prompt))
                        
                        # Configuration with Thread ID
                        config = {"configurable": {"thread_id": st.session_state.thread_id}}
                        
                        # Use the Async Bridge for Streaming
                        with st.spinner("Atlas is thinking..."):
                            # We pass the generator function to st.write_stream
                            response_stream = run_async_stream(st.session_state.agent_executor, {"messages": input_messages}, config)
                            
                            final_response = st.write_stream(response_stream)
                        
                        # Add to history
                        st.session_state.messages.append({"role": "assistant", "content": final_response})
                        save_chat_history(st.session_state.messages, st.session_state.thread_id)
                        
                    except Exception as e:
                        st.error(f"Error processing: {e}")
            else:
                st.error("Please configure API_KEY in .env or secrets.")

def setup_page(title, icon):
    """
    Sets up the page configuration, loads CSS, renders navbar and sidebar chat.
    """
    st.set_page_config(page_title=f"{title} | André Amorim", page_icon=icon, layout="wide")
    load_css()
    render_navbar()
    render_sidebar_chat()

def card(title, content, date=None, image=None):
    """
    Displays a card with a title, content, optional date, and optional image.
    """
    with st.container():
        st.markdown(f"""
        <div class="stCard">
            <h3>{title}</h3>
            {f'<p style="color: #666; font-size: 0.9em;">{date}</p>' if date else ''}
            <p>{content}</p>
        </div>
        """, unsafe_allow_html=True)
