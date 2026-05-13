# 🎨 Phase 3 — Web UI

> **Goal:** Build a clean, beginner-friendly web interface so non-developers can use PromptLens without touching a terminal. This is what makes the project accessible to researchers, students, and writers.

---

## 📦 What You'll Build

- A single-page HTML/CSS/JS frontend
- Prompt input box
- Model selector (checkboxes)
- Metric selector (checkboxes)
- Side-by-side results comparison table
- Score visualization (progress bars / color coding)
- "Copy response" button per model

---

## 🗂️ Folder Structure (Phase 3)

```
promptlens/
├── backend/
├── frontend/
│   ├── index.html        ← Main UI page
│   ├── style.css         ← Styling
│   ├── app.js            ← Fetch calls to backend API
│   └── assets/
│       └── logo.svg
└── README.md
```

---

## ⚙️ Setup

No npm, no build step. Just open the file:

```bash
# Make sure backend is running first (from Phase 2)
uvicorn backend.main:app --reload --port 8000

# Then open the UI
open frontend/index.html
# or just drag it into your browser
```

---

## 🖥️ UI Features

| Feature | Description |
|---|---|
| **Prompt Box** | Large textarea for entering the prompt |
| **Model Picker** | Toggle which LLMs to test against |
| **Metric Picker** | Choose which metrics to score on |
| **Run Button** | Sends to backend, shows loading state |
| **Results Panel** | Side-by-side model responses with scores |
| **Score Bars** | Visual progress bars for each metric score |
| **Copy Button** | One-click copy for each model's response |

---

## 🎨 Design Principles

- **No login required** — open and use
- **Mobile friendly** — works on phone too
- **Dark mode supported** — respects system preference
- **Zero frameworks** — plain HTML/CSS/JS, no React/Vue needed

---

## ✅ Phase 3 Checklist

- [ ] `index.html` opens in browser without errors
- [ ] Prompt can be typed and submitted
- [ ] Results show up for each selected model
- [ ] Scores render as visual bars
- [ ] Works on mobile screen size
- [ ] Loading spinner shows while waiting for API

---

## 📸 Screenshots

> Add screenshots here after building the UI. This is important for your README and GitHub social preview!

---

## ➡️ Next: [Phase 4 — Open Source Polish](../phase-4/README.md)
## ⬅️ Prev: [Phase 2 — FastAPI Backend](../phase-2/README.md)

---

## 🤝 Contributing to Phase 3

**Good first issues for this phase:**
- Add a dark/light mode toggle button
- Add export results as CSV
- Add a "share results" link generator
- Improve mobile layout
- Add keyboard shortcut (Ctrl+Enter) to run
