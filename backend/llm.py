import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def ask_llm(prompt):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://doc-intelligence-esa5ngepmuwfw6x3ukyytu.streamlit.app",
            "X-Title": "Doc Intelligence"
        },
        json={
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "You answer using only provided document context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("RAW:", response.text)

    if response.status_code != 200:
        return response.text

    return response.json()["choices"][0]["message"]["content"]

    return resp_json["choices"][0]["message"]["content"]
