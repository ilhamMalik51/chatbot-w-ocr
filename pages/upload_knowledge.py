import os
import streamlit as st

from dotenv import load_dotenv
from google import genai
from google.genai import types
from db.vector_db import VectorDB

from services.ocr import extract_text_from_image

load_dotenv()

st.title("Upload Your Online Food Receipt !")
file = st.file_uploader(label="Upload your image ...")

if "vector_db" not in st.session_state:
    st.session_state.vector_db = VectorDB()

if file != None:
    text = extract_text_from_image(file.read())
    
    # google_client = genai.Client(api_key=os.getenv("API_KEY"))
    # emb_value = google_client.models.embed_content(
    #     model="gemini-embedding-001",
    #     contents=text,
    #     config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")).embeddings[0].values
    
    # st.session_state.vector_db.add(vecs=emb_value, content=text)

    st.write(f"## There are {st.session_state.vector_db.get_docs_size()} documents")

    st.write("## Page Content")
    st.write(text)