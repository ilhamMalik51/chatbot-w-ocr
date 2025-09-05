import os
import time
import streamlit as st

from google import genai
from google.genai import types
from datetime import datetime

from db.myvectordb import VectorClient

def retrieve_data(text, llm):
    """Retrieve data from vector database."""
    vector_client = VectorClient(os.getenv('VECTORDB_ENDPOINT'))
    query_vector = llm.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")).embeddings[0].values
    
    return vector_client.search(vector=query_vector, k=5)

def generate_search_query(text_input, llm):
    """Rephrase the text input so the context retrieval is more relevant"""
    datetime_str = datetime.now().strftime("%Y-%m-%d")
    system_prompt = [
        "You are a professional at making search query."
    ]
    prompt_input = """Rephrase the following query so that it can retrieve document in database more accurately. If not needed return the user question as is.
    
    ### Today's Date:
    {datetime_str}

    ### Document Schema:
    {{
        "date_order": the order date,
        "foods": the food order,
        "restaurant": the restauran of the food order,
        "total_expense": the total of expenses
    }}

    ### User's Question:
    {text_input}""".format(datetime_str=datetime_str, text_input=text_input)
    response = llm.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_input,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3
        ),
    )

    return response.text

def response_generator(text_input, llm):
    """Generate response with predifine system prompt and prompt"""
    datetime_str = datetime.now().strftime("%Y-%m-%d")
    rephrase_input = generate_search_query(text_input=text_input, llm=llm)
    print(f"Rephrase input {rephrase_input}")
    relevant_context = retrieve_data(text=rephrase_input, llm=llm)
    
    context_str = "\n\n### FOOD RECEIPT\n".join([ doc[0]['content'] for doc in relevant_context ])
    print(f"Context: {context_str}")
    
    system_prompt = [
        "You are a helpful assistant.",
        "Your answer should be from the provided historical receipt and concise",
        f"Today's Date {datetime_str}"
    ]
    prompt_input = f"""Use the following historical food online receipt to improve your answer.
    
    Context:
    {context_str}

    Question:
    {text_input}"""

    response = llm.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt_input,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3
        ),
    )

    for word in response:
        yield word.text
        time.sleep(0.05)