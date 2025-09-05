import time
import streamlit as st

from google import genai
from google.genai import types
from datetime import datetime

def retrieve_data(text, llm):
    query_vector = llm.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")).embeddings[0].values
    
    return st.session_state.vector_db.search(query_vector=query_vector, k=3)

def response_generator(text_input, llm):
    relevant_context = retrieve_data(text=text_input, llm=llm)
    context_str = "\n\n### FOOD RECEIPT".join([ doc[0]['content'] for doc in relevant_context ])
    print(f"Context: {context_str}")

    datetime_str = datetime.now().strftime("%Y-%m-%d")
    system_prompt = [
        "You are a helpful assistant.",
        "Your answer should be from the provided context, concise, and straight to the point.",
        f"Today's Date {datetime_str}"
    ]

    prompt_input = f"""Use the following context and chat history to improve your answer.
    
    Context:
    {context_str}

    Question:
    {text_input}"""

    response = llm.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=prompt_input,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0
        ),
    )

    for word in response:
        yield word.text