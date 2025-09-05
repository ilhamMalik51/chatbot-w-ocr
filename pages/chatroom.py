import os
import streamlit as st

from google import genai
from services.response_generator import response_generator

st.title("Welcome to AI Application Chatroom")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Here ..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt, st.session_state.google_client))

    st.session_state.messages.append({"role": "assistant", "content": response})