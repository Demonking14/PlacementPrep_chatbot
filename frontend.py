from backend import workflow, db
from langchain_core.messages import HumanMessage
import streamlit as st
import uuid

def generateThread():
    thread_id = uuid.uuid4()
    return str(thread_id);

def resetMesssage():
     thread_id = generateThread()
     st.session_state['thread_id']=thread_id
     add_threads(threadid=thread_id);
     st.session_state['msg_history']  = []
     
def add_threads(threadid):
    if threadid not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(threadid);     
        
def load_all_mongo_thread():
    collection = db["checkpointing_db.checkpoints"]
    threads = collection.distinct("thread_id")
    return[uuid.UUID(t) if isinstance(t, str) else t for t in threads]
    
     
def loadChats(threadid):
    return workflow.get_state(config={"configurable":{"thread_id": threadid}}).values.get('message', [])



if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generateThread()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread'] = load_all_mongo_thread()
    
if 'msg_history' not in st.session_state:
    st.session_state['msg_history'] = []

CONFIG = {"configurable" : {"thread_id" : st.session_state['thread_id']}}
add_threads(st.session_state['thread_id'])

st.sidebar.header("My Conversations")
if st.sidebar.button("New Chat"):
    resetMesssage()
 

st.sidebar.header("Message history")
for thread_id in st.session_state['chat_thread'][::]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = loadChats(threadid=thread_id)
        temp_msg = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'ai'
            temp_msg.append({'role': role, 'message': msg.content})
        st.session_state['msg_history'] = temp_msg

for message in st.session_state['msg_history']:
    with st.chat_message(message['role']):
        st.text(message['message'])

user_input = st.chat_input("Type your queries here")

if user_input:
    st.session_state['msg_history'].append({"role" : 'user' , "message":user_input })
    with st.chat_message('user'):
        st.text(user_input)
    
    with st.chat_message('ai'):
        ai_message = ""
        for message_chunk , metadata in workflow.stream(
        {"message" : [HumanMessage(content=user_input)]},
        config=CONFIG,
        stream_mode='messages'
        ):
            ai_message += message_chunk.content
            st.write_stream([message_chunk.content]);
        st.session_state['msg_history'].append({"role":"ai" , "message":ai_message})

