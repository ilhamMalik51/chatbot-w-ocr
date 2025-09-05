import os
import streamlit as st

from dotenv import load_dotenv
from google import genai
from google.genai import types

from services.ocr import (
    extract_text_from_image, store_data_to_db, extract_insight_from_text
)

load_dotenv()

st.title("Upload Your Online Food Receipt !")
file = st.file_uploader(label="Upload your image ...")

if "google_client" not in st.session_state:
    st.session_state.google_client = genai.Client(api_key=os.getenv("API_KEY"))

if file != None:
    text = extract_text_from_image(file.read())
    insight_text = extract_insight_from_text(text, llm=st.session_state.google_client)
    current_size = store_data_to_db(text=insight_text, llm=st.session_state.google_client)

    st.write(f"## There are {current_size} documents")
    st.write("## Extracted Insight Text")
    st.markdown(insight_text)