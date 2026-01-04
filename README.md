# 🚀 André Amorim | Professional Portfolio & Atlas AI Agent

> *"Labor omnia vincit, per aspera ad astra."*

Welcome to the **Professional Portfolio of André Amorim** (Baldros).
This project goes beyond a static curriculum: it is an interactive platform built with **Streamlit** that integrates **Atlas**, an advanced AI Agent designed to represent, explain, and demonstrate the author's technical capabilities in real-time.

---

## 🎯 Project Purpose

The main goal of this project is to build authority and demonstrate practical expertise in **Software Engineering** and **Artificial Intelligence**.
It operates on two pillars:

1.  **Professional Showcase**: A dynamic web application that presents Experience, Academic Background, and Skills in an engaging format.
2.  **Atlas Intelligent Agent**: An embedded AI agent capable of interacting with recruiters and visitors, answering questions, and proving skills by accessing verified evidence (documents and repositories).

## 🧠 The Atlas Agent

**Atlas** is the core intelligence of this portfolio. It is not just a chatbot, but a **Tool-Use Agent** built with modern architecture:

-   **Architecture**: Built on [LangChain](https://docs.langchain.com/oss/python/langchain/overview) for reliable event-driven orchestration.
-   **Model-Context Protocol (MCP)**: Integrates with external contexts (like GitHub) via async MCP servers.
-   **Local & Remote Tools**: Capable of reading local markdown documentation, list files, analyze tabular data (CSV/Excel), and send emails.
-   **Async-Sync Bridge**: Implements a custom bridge to run asynchronous MCP tools within the synchronous Streamlit environment.

### Key Capabilities

-   **Contextual Awareness**: Reads deeply into `Context/files` (Markdown) to answer questions about André's career.
-   **Data Analysis**: Can load and analyze tables (CSVs) on demand to extract specific metrics.
-   **Active Communication**: Capable of sending emails directly to André for inquiries or opportunities.
-   **Real-Time Streaming**: Provides a typing-effect response for a natural user experience.

## 🛠️ Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **AI Framework**: [LangChain](https://www.langchain.com/) & [LangGraph](https://langchain-ai.github.io/langgraph/)
-   **LLM Provider**: OpenAI (GPT-4o / GPT-5-nano)
-   **Tools/Integration**: Pandas, Asyncio, SMTP (Gmail), MCP Client (GitHub Copilot API).

## 📂 Project Structure

```bash
PersonalSite/
├── app.py                  # Main Application Entry Point (Streamlit)
├── utils.py                # UI Helpers, Chat Rendering, Async Bridge
├── .env                    # Environment Variables (Keys, Tokens)
├── pages/                  # Additional Streamlit Pages (Skills, Experience, etc.)
└── ai_agent/               # The Brain of Atlas
    ├── core.py             # Agent Logic & Graph Construction
    ├── behavior.py         # System Prompt & Personality (Atlas Persona)
    ├── tools.py            # Tool Definitions & Pydantic Schemas
    ├── functions.py        # Core Logic for Tools (Email, Pandas, File I/O)
    └── Context/            # Knowledge Base (Markdown Files & Data)
```

## 🚀 Getting Started

### Prerequisites

-   Python 3.10+
-   API Keys: `OPENAI_API_KEY`, `GITHUB_ACCESS_TOKEN`, `EMAIL_USER/PASSWORD` (for email tool).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Baldros/PersonalSite.git
    cd PersonalSite
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure `.env`:
    Create a `.env` file in the root with your credentials.

4.  Run the application:
    ```bash
    streamlit run app.py
    ```

## 📬 Contact

-   **LinkedIn**: [André Amorim](https://www.linkedin.com/in/andr%C3%A9-amorim-73943bb7/)
-   **GitHub**: [Baldros](https://github.com/Baldros)
-   **Lattes**: [CV Lattes](https://lattes.cnpq.br/9153087289739313)

---
*Built with ❤️ and Code by André Amorim.*
