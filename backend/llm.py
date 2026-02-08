import requests
import streamlit as st

def ask_llm(prompt):

    key = st.secrets["OPENROUTER_API_KEY"]

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://doc-intelligence-esa5ngepmuwfw6x3ukyytu.streamlit.app",
            "X-Title": "Doc Intelligence"
        },
        json={
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [
                {"role": "system", "content": "You answer using only provided document context."},
                {"role": "user", "content": prompt}
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    if response.status_code != 200:
        return response.text

    return response.json()["choices"][0]["message"]["content"]
