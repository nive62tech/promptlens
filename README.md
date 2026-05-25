# 🔬 PromptLens

> **Local-first, beginner-friendly LLM Prompt Evaluation Toolkit**

Compare and evaluate responses from multiple Large Language Models
side-by-side — with readability, sentiment, and length scoring.
Your prompts never leave your machine.

---

## ✨ Features

- 🤖 **Multi-model support** — Qwen 2.5, Gemini Pro, and more
- 📊 **Quality metrics** — Readability, Sentiment, Length
- 🔒 **Privacy-first** — 100% local, no data sent to any server
- 🌐 **Clean Web UI** — no coding knowledge needed
- ⚡ **REST API** — integrate with any frontend or tool
- 🧩 **Modular design** — add new models and metrics easily

---

## 🖥️ Demo

> Run it locally in 3 commands — see below

![PromptLens UI](https://raw.githubusercontent.com/nive62tech/promptlens/main/docs/screenshot.png)

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/nive62tech/promptlens.git
cd promptlens

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API keys
copy .env.example .env
# Edit .env and add your keys

# 5. Run the server
python -m uvicorn backend.main:app --reload --port 8000

# 6. Open in browser
# Go to http://localhost:8000
```

---

## 🔑 API Keys Needed

| Key | Where to get | Cost |
|---|---|---|
| `GEMINI_API_KEY` | aistudio.google.com | Free |
| `HF_API_KEY` | huggingface.co/settings/tokens | Free |
| `OPENAI_API_KEY` | platform.openai.com | Optional |

> ⚠️ Your keys are stored in `.env` locally and never leave your machine.

---

## 📁 Project Structure

promptlens/
├── backend/
│   ├── main.py              ← FastAPI app
│   ├── runner.py            ← Core evaluation engine
│   ├── connectors/          ← One file per LLM
│   │   ├── gemini_connector.py
│   │   └── hf_connector.py
│   └── metrics/             ← One file per metric
│       ├── length.py
│       ├── readability.py
│       └── sentiment.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── phase-1/README.md
├── phase-2/README.md
├── phase-3/README.md
├── phase-4/README.md
├── .env.example
└── requirements.txt

---

## 🤝 Contributing

We welcome contributions of all kinds!

**Easiest ways to contribute:**
- Add a new metric (e.g. toxicity, coherence)
- Add a new LLM connector (e.g. Mistral, Cohere)
- Improve the UI (dark/light toggle, CSV export)
- Write tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guide.

---

## 🗺️ Roadmap

- [ ] Add toxicity metric
- [ ] Add Mistral connector
- [ ] Add CSV export
- [ ] Add prompt history
- [ ] Docker support
- [ ] HuggingFace Spaces demo

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## 🙏 Built by

[@nive62tech](https://github.com/nive62tech) — Final Year AIML Student

