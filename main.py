import streamlit as st

upload_file = st.Page("./pages/upload_knowledge.py", title="Upload AI Knowledge")
chatroom = st.Page("./pages/chatroom.py", title="Chat with AI")

pg = st.navigation([chatroom, upload_file])

pg.run()