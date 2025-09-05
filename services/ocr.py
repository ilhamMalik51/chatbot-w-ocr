import io, os
import pytesseract

from google.genai import types
from PIL import Image
from db.myvectordb import VectorClient


def extract_text_from_image(image_bytes: bytes):
    """Extract image from the given path"""
    image_obj = Image.open(io.BytesIO(image_bytes))

    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    result = pytesseract.image_to_string(image_obj, lang="eng")

    return result

def extract_insight_from_text(text: str, llm: object):
    """Extract insight from the text."""
    system_prompt = [
        "You are a JSON extractor professional.",
        "You can extract key informations from online food receipt."
    ]
    prompt_input = """Extract the following free text into json format data.
    ###Text:
    {text}

    ###JSON Format:
    {{
        "date_order": the order date,
        "foods": the food order,
        "restaurant": the restauran of the food order,
        "total_expense": the total of expenses
    }}""".format(text=text)
    response = llm.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt_input,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0
        ),
    )

    return response.text

def store_data_to_db(text: str, llm: object):
    """Insert data to the database"""
    vector_client = VectorClient(endpoint=os.getenv('VECTORDB_ENDPOINT'))
    emb_value = llm.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")).embeddings[0].values
    
    vector_client.insert_document(vector=emb_value, content=text)

    return vector_client.get_document_size()