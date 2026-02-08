import requests

def ask_llm(prompt, api_key):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
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
