import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def ask_llm(prompt):
    print("SECRET EXISTS:", bool(OPENROUTER_API_KEY))

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://doc-intelligence.streamlit.app",
        "X-Title": "Doc Intelligence"
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You answer using only provided document context."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    resp_json = response.json()

    if "choices" not in resp_json:
        return str(resp_json)

    return resp_json["choices"][0]["message"]["content"]
