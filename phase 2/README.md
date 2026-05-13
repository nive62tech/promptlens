# 🌐 Phase 2 — FastAPI Backend

> **Goal:** Wrap the Phase 1 core engine in a clean REST API using FastAPI. This turns PromptLens from a script into a real service that any frontend can talk to.

---

## 📦 What You'll Build

| Endpoint | Method | What It Does |
|---|---|---|
| `/evaluate` | POST | Send a prompt, get back scores from all models |
| `/models` | GET | List all available LLM connectors |
| `/metrics` | GET | List all available metrics |
| `/health` | GET | Health check — is the server running? |

---

## 🗂️ Folder Structure (Phase 2)

```
promptlens/
├── backend/
│   ├── main.py           ← FastAPI app lives here
│   ├── runner.py
│   ├── models/
│   │   └── schemas.py    ← Pydantic request/response models
│   ├── connectors/
│   └── metrics/
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

Make sure Phase 1 is working first, then:

```bash
pip install fastapi uvicorn

# Run the API server
uvicorn backend.main:app --reload --port 8000
```

Server will start at: `http://localhost:8000`

API docs (auto-generated): `http://localhost:8000/docs`

---

## 📡 API Usage

### Evaluate a Prompt

```bash
curl -X POST http://localhost:8000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain black holes in simple terms",
    "models": ["gpt-3.5-turbo", "gemini-pro"],
    "metrics": ["length", "readability", "sentiment"]
  }'
```

### Sample Response

```json
{
  "prompt": "Explain black holes in simple terms",
  "results": [
    {
      "model": "gpt-3.5-turbo",
      "response": "A black hole is a region in space...",
      "scores": {
        "length": 78,
        "readability": 82,
        "sentiment": "neutral"
      }
    },
    {
      "model": "gemini-pro",
      "response": "Black holes are formed when...",
      "scores": {
        "length": 91,
        "readability": 70,
        "sentiment": "neutral"
      }
    }
  ]
}
```

---

## ✅ Phase 2 Checklist

- [ ] FastAPI server starts without errors
- [ ] `/health` returns `{"status": "ok"}`
- [ ] `/evaluate` returns results for at least 2 models
- [ ] `/docs` page renders correctly
- [ ] Pydantic schemas validate bad inputs properly

---

## 🔐 Security Notes

- API keys are loaded from `.env` — never hardcoded
- No prompt data is logged or stored
- CORS is configured to allow only localhost in dev mode

---

## ➡️ Next: [Phase 3 — Web UI](../phase-3/README.md)
## ⬅️ Prev: [Phase 1 — Core Engine](../phase-1/README.md)

---

## 🤝 Contributing to Phase 2

**Good first issues for this phase:**
- Add request rate limiting
- Add a `/history` endpoint (session-based, local only)
- Add response caching to avoid duplicate API calls
- Add input validation for prompt length limits
