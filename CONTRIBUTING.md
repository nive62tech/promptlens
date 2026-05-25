# 🤝 Contributing to PromptLens

Thank you for considering contributing! PromptLens is designed
to be beginner-friendly for contributors too.

---

## 🧭 Where to Start

Check the Issues tab on GitHub for tickets labeled:
- `good first issue` — perfect for first-time contributors
- `help wanted` — we need help here
- `documentation` — improve docs

---

## ➕ Adding a New Metric

1. Create a new file in `backend/metrics/`
   e.g. `backend/metrics/toxicity.py`

2. Follow this exact structure:
```python
def score_toxicity(text: str) -> dict:
    # your scoring logic here
    return {"label": "non-toxic", "score": 0.02}
```

3. Register it in `backend/runner.py`:
```python
from backend.metrics.toxicity import score_toxicity

METRICS = {
    "length": score_length,
    "readability": score_readability,
    "sentiment": score_sentiment,
    "toxicity": score_toxicity,   # add this
}
```

4. Add it to the UI in `frontend/index.html`

---

## ➕ Adding a New LLM Connector

1. Create a new file in `backend/connectors/`
   e.g. `backend/connectors/cohere_connector.py`

2. Follow this exact structure:
```python
import os

def query_cohere(prompt: str) -> str:
    # your API call here
    return "response text"
```

3. Register it in `backend/runner.py`:
```python
from backend.connectors.cohere_connector import query_cohere

CONNECTORS = {
    "gemini-pro": query_gemini,
    "qwen-7b": query_huggingface,
    "cohere": query_cohere,   # add this
}
```

4. Add it to the UI in `frontend/index.html`

---

## 🔧 Setup for Development

```bash
git clone https://github.com/nive62tech/promptlens.git
cd promptlens
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Add your API keys to .env
python -m uvicorn backend.main:app --reload --port 8000
```

---

## 📬 Submitting a Pull Request

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature-name`
3. Make your changes
4. Commit: `git commit -m "feat: add toxicity metric"`
5. Push: `git push origin feat/your-feature-name`
6. Open a Pull Request on GitHub

---

## 💬 Questions?

Open an issue and ask — no question is too small!