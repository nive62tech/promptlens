# 🎨 Phase 3 — Web UI

> **Goal:** A clean, beginner-friendly web interface so anyone can use
> PromptLens without touching a terminal.

---

## ✅ What Was Built

| Feature | Description |
|---|---|
| Prompt box | Large textarea for entering the prompt |
| Model picker | Toggle which LLMs to test against |
| Metric picker | Choose which metrics to score on |
| Run button | Sends to backend, shows loading state |
| Results panel | Side-by-side model responses with scores |
| Score bars | Visual progress bars for readability and length |
| Sentiment badge | Color-coded positive / neutral / negative |
| Copy button | One-click copy for each model response |
| Keyboard shortcut | Ctrl+Enter to run evaluation |

---

## 🗂️ Files Added in This Phase
frontend/
├── index.html     ← Main UI page
├── style.css      ← Dark theme styling
└── app.js         ← Fetch calls to backend API

---

## ⚙️ Setup

No npm, no build step needed.

```bash
# Step 1 — Start the backend first
python -m uvicorn backend.main:app --reload --port 8000

# Step 2 — Open the UI
# Just go to this URL in Chrome:
http://localhost:8000
```

---

## 🖥️ How to Use

1. Open `http://localhost:8000` in your browser
2. Type your prompt in the text box
3. Select which models to evaluate
4. Select which metrics to score on
5. Click **Run Evaluation** or press **Ctrl+Enter**
6. Wait 10–20 seconds for results
7. See side-by-side responses with scores

---

## 🎨 Design Decisions

- **Dark theme** — easier on the eyes for developers
- **No framework** — plain HTML/CSS/JS, zero setup for contributors
- **Served through FastAPI** — avoids CORS issues with file:// protocol
- **Mobile responsive** — works on phone screens too

---

## ✅ Phase 3 Checklist

- [x] UI opens at `http://localhost:8000`
- [x] Prompt can be typed and submitted
- [x] Results show for each selected model
- [x] Scores render as visual bars
- [x] Sentiment shows as colored badge
- [x] Copy button works
- [x] Ctrl+Enter shortcut works
- [x] Mobile responsive layout

---

## 🤝 Good First Issues for Contributors

- Add dark/light mode toggle button
- Add export results as CSV
- Add response word count comparison chart
- Improve mobile layout
- Add loading skeleton instead of text spinner
- Add prompt history (last 5 prompts dropdown)
- Add character counter for prompt input

## ➡️ Next: [Phase 4 — Open Source Polish](../phase-4/README.md)
## ⬅️ Prev: [Phase 2 — FastAPI Backend](../phase-2/README.md)