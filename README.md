# 🎯 Placement Prep AI Assistant

A conversational AI chatbot built with LangGraph and Streamlit to help students prepare for placements. It explains DSA concepts, system design, architecture patterns, and gives hints without spoiling solutions.

## ✨ Features

- Multi-turn conversation with persistent memory
- Placement-focused responses — DSA hints, system design explanations, architecture guidance
- Clean chat UI with message history
- Session-based conversation isolation

## 🛠 Tech Stack

- **LangGraph** — graph-based AI workflow
- **Google Gemini 2.5 Flash** — LLM
- **Streamlit** — frontend UI
- **LangChain** — message handling
- **InMemorySaver** — conversation checkpointing

## 🧠 How Memory Works
This chatbot maintains conversation history across multiple turns using three key concepts:
Message State with add_messages
Instead of replacing the message list on every turn, add_messages appends new messages to the existing state — maintaining the full conversation history as [message1, message2, message3, ...] rather than overwriting previous messages.
Checkpointing with InMemorySaver
The LangGraph workflow is divided into checkpoints at each node. After every step, the current state is saved as a checkpoint. InMemorySaver stores these checkpoints in RAM, allowing the graph to retrieve and resume any conversation from its last known state.
Session Isolation with thread_id
Every conversation is assigned a unique thread_id via the config object. When retrieving checkpoint history, LangGraph uses this ID to fetch only the relevant conversation — preventing any cross-contamination between different users' sessions.

Production Note: InMemorySaver is ephemeral — history is lost on server restart. For production, replace with SqliteSaver or PostgresSaver for persistent storage.

## 🚀 How to Run

1. Clone the repo
```bash
git clone <your-repo-url>
cd placement-prep-assistant
```

2. Install dependencies
```bash
pip install langgraph langchain-google-genai streamlit python-dotenv
```

3. Add your API key
```bash
# create .env file
GOOGLE_API_KEY=your_key_here
```

4. Run the app
```bash
streamlit run frontend.py
```

## 📁 Project Structure

```
├── frontend.py      # Streamlit UI
├── backend.py       # LangGraph workflow
├── .env             # API keys (not committed)
└── README.md
```
