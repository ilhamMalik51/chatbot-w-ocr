import os
import streamlit as st

from google import genai
from db.vector_db import VectorDB

from dotenv import load_dotenv
from services.response_generator import response_generator

load_dotenv()

st.title("Welcome to AI Application Chatroom")
google_client = genai.Client(api_key=os.getenv("API_KEY"))

if "vector_db" not in st.session_state:
    st.session_state.vector_db = VectorDB()
    st.session_state.vector_db.init_seed_data()
    st.write(f"### Seed Data Loaded {st.session_state.vector_db.get_docs_size()} Documents")

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
        response = st.write_stream(response_generator(prompt, google_client))

    st.session_state.messages.append({"role": "assistant", "content": response})