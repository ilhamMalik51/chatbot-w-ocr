import os
import streamlit as st

from google import genai

from dotenv import load_dotenv

load_dotenv()

upload_file = st.Page("./pages/upload_knowledge.py", title="Upload AI Knowledge")
chatroom = st.Page("./pages/chatroom.py", title="Chat with AI")

if "google_client" not in st.session_state:
    st.session_state.google_client = genai.Client(api_key=os.getenv("API_KEY"))

pg = st.navigation([chatroom, upload_file])
pg.run()