from dotenv import load_dotenv
from backend.connectors.gemini_connector import query_gemini
from backend.connectors.hf_connector import query_huggingface
from backend.metrics.length import score_length
from backend.metrics.readability import score_readability
from backend.metrics.sentiment import score_sentiment

load_dotenv()

CONNECTORS = {
    "gemini-pro": query_gemini,
    "qwen-7b": query_huggingface,
}

METRICS = {
    "length": score_length,
    "readability": score_readability,
    "sentiment": score_sentiment,
}

def run_evaluation(prompt: str, models: list, metrics: list):
    results = []
    for model in models:
        if model not in CONNECTORS:
            continue
        try:
            response = CONNECTORS[model](prompt)
            scores = {m: METRICS[m](response) for m in metrics if m in METRICS}
            results.append({
                "model": model,
                "response": response,
                "scores": scores
            })
        except Exception as e:
            results.append({
                "model": model,
                "response": f"Error: {str(e)[:80]}",
                "scores": {}
            })
    return results