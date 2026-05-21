# 🌐 Phase 2 — FastAPI Backend

> **Goal:** Wrap the Phase 1 core engine in a clean REST API using FastAPI.

---

## ✅ What Was Built

| Endpoint | Method | What It Does |
|---|---|---|
| `/health` | GET | Returns server status |
| `/models` | GET | Lists available LLM connectors |
| `/metrics` | GET | Lists available metrics |
| `/evaluate` | POST | Sends prompt, returns scored results |
| `/docs` | GET | Auto-generated API documentation |

---

## 🗂️ Files Added in This Phase
backend/
├── main.py              ← FastAPI app
└── models/
├── init.py
└── schemas.py       ← Pydantic request/response models

---

## ⚙️ Setup

```bash
# Install dependencies
pip install fastapi uvicorn aiofiles

# Run the server
python -m uvicorn backend.main:app --reload --port 8000
```

Server runs at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

---

## 📡 Sample Request

```bash
curl -X POST http://localhost:8000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain black holes in simple terms",
    "models": ["qwen-7b"],
    "metrics": ["length", "readability", "sentiment"]
  }'
```

## 📡 Sample Response

```json
{
  "prompt": "Explain black holes in simple terms",
  "results": [
    {
      "model": "qwen-7b",
      "response": "A black hole is a region in space...",
      "scores": {
        "length": {"words": 156, "chars": 880},
        "readability": {"flesch_reading_ease": 64.5, "grade_level": 8.5},
        "sentiment": {"label": "neutral", "score": 0.073}
      }
    }
  ]
}
```

---

## 🔐 Security

- API keys loaded from `.env` — never hardcoded
- No prompt data is logged or stored
- CORS configured to allow all origins in dev mode

---

## ✅ Phase 2 Checklist

- [x] FastAPI server starts without errors
- [x] `/health` returns `{"status": "ok"}`
- [x] `/evaluate` returns results with scores
- [x] `/docs` page renders correctly
- [x] Pydantic schemas validate requests

---

## 🤝 Good First Issues for Contributors

- Add request rate limiting
- Add a `/history` endpoint (session-based, local only)
- Add response caching to avoid duplicate API calls
- Add input validation for prompt length limits
- Write unit tests for all endpoints

## ➡️ Next: [Phase 3 — Web UI](../phase-3/README.md)
## ⬅️ Prev: [Phase 1 — Core Engine](../phase-1/README.md)