import os
import requests

def query_huggingface(prompt: str) -> str:
    api_key = os.getenv("HF_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300
    }

    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(f"HF error {response.status_code}: {response.text[:150]}")

    return response.json()["choices"][0]["message"]["content"]