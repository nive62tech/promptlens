# 🔬 Phase 1 — Core Engine

> **Goal:** Build the heart of PromptLens — the prompt runner, LLM connectors, and scoring metrics. No UI yet. Just a working Python backend you can test from the terminal.

---

## 📦 What You'll Build

| Module | File | What It Does |
|---|---|---|
| Prompt Runner | `backend/runner.py` | Sends prompts to LLMs, collects responses |
| OpenAI Connector | `backend/connectors/openai_connector.py` | Connects to GPT models |
| Gemini Connector | `backend/connectors/gemini_connector.py` | Connects to Google Gemini |
| HuggingFace Connector | `backend/connectors/hf_connector.py` | Connects to free HF models |
| Length Metric | `backend/metrics/length.py` | Scores response by word/char count |
| Readability Metric | `backend/metrics/readability.py` | Flesch-Kincaid readability score |
| Sentiment Metric | `backend/metrics/sentiment.py` | Positive / Negative / Neutral scoring |

---

## 🗂️ Folder Structure (Phase 1)

```
promptlens/
├── backend/
│   ├── runner.py
│   ├── connectors/
│   │   ├── __init__.py
│   │   ├── openai_connector.py
│   │   ├── gemini_connector.py
│   │   └── hf_connector.py
│   └── metrics/
│       ├── __init__.py
│       ├── length.py
│       ├── readability.py
│       └── sentiment.py
├── .env.example
├── requirements.txt
└── test_runner.py
```

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/promptlens.git
cd promptlens

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup your API keys
cp .env.example .env
# Edit .env and add your keys
```

---

## 🔑 .env Setup

```env
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
HF_API_KEY=your_huggingface_key_here
```

> ⚠️ **Your prompts and keys NEVER leave your machine. Everything runs locally.**

---

## 🧪 Testing Phase 1

```bash
python test_runner.py
```

Expected output:
```
✅ Prompt sent to: gpt-3.5-turbo
✅ Prompt sent to: gemini-pro
📊 Scores:
  - Length Score: 72/100
  - Readability Score: 65/100
  - Sentiment: Positive
```

---

## ✅ Phase 1 Checklist

- [ ] Repo cloned and virtual env working
- [ ] `.env` file configured with at least 1 API key
- [ ] `runner.py` sends prompt and gets response
- [ ] At least 2 connectors working
- [ ] All 3 metrics returning scores
- [ ] `test_runner.py` passes

---

## ➡️ Next: [Phase 2 — FastAPI Backend](../phase-2/README.md)

---

## 🤝 Contributing to Phase 1

Want to add a new metric or connector? See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Good first issues for this phase:**
- Add a new metric (e.g., toxicity, coherence)
- Add a new LLM connector (e.g., Mistral, Cohere)
- Improve error handling in `runner.py`
