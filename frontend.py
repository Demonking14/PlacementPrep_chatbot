from backend import workflow
from langchain_core.messages import HumanMessage
import streamlit as st

CONFIG = {"configurable" : {"thread_id" : "thread1"}}

if 'msg_history' not in st.session_state:
    st.session_state['msg_history'] = [];
else: 
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

