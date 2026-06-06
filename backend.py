from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langgraph.graph.message import  add_messages
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.mongodb import MongoDBSaver
from pymongo import MongoClient
import os
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash');

class messageState(TypedDict):
    message: Annotated[list[BaseMessage] , add_messages]

def chatMsg(state:messageState)->messageState:
    prompt = f"You are a Placement helper bot who gives hint , explain concepts of system design , architecture  and help in preparation of student's placement journey \n User will give input and you have to give reponse based on it \n User input: ${state['message']}"
    response = model.invoke(prompt);
    return {'message':  [AIMessage(content=response.content)]}

client = MongoClient(mongo_uri)
db = client["checkpointing_db"]
checkpoint = MongoDBSaver(db);

graph = StateGraph(messageState)
graph.add_node("chatMsg", chatMsg)
graph.add_edge(START, "chatMsg")
graph.add_edge("chatMsg" , END)

# checkpoint = InMemorySaver();
workflow = graph.compile(checkpointer=checkpoint)
