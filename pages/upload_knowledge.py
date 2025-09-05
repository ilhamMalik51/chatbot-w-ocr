import os
import streamlit as st

from dotenv import load_dotenv
from google import genai
from google.genai import types

from services.ocr import (
    extract_text_from_image, store_data_to_db
)

load_dotenv()

st.title("Upload Your Online Food Receipt !")
file = st.file_uploader(label="Upload your image ...")

if file != None:
    text = extract_text_from_image(file.read())
    current_size = store_data_to_db(text=text, llm=st.session_state.google_client)

    st.write(f"## There are {current_size} documents")

    st.write("## Page Content")
    st.write(text)