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

<!-- Write this section yourself — you explained it perfectly already -->

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
