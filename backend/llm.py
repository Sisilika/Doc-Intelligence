import requests
import streamlit as st

def ask_llm(prompt):

    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {"role": "system", "content": "You answer using only provided document context."},
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        return response.text

    return response.json()["choices"][0]["message"]["content"]
