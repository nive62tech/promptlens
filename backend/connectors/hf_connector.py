import os
from huggingface_hub import InferenceClient

def query_huggingface(prompt: str) -> str:
    client = InferenceClient(api_key=os.getenv("HF_API_KEY"))

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )

    return response.choices[0].message.content