# 🚀 Phase 4 — Open Source Polish & Launch

> **Goal:** Turn the working project into a proper open source repository that welcomes contributors, gets starred, and gets shared. This phase is about community, documentation, and visibility.

---

## 📦 What You'll Do

| Task | What It Achieves |
|---|---|
| Write proper README with GIF demo | First impression for visitors |
| Write CONTRIBUTING.md | Tells contributors exactly what to do |
| Add GitHub Issue Templates | Structures bug reports and feature requests |
| Add GitHub Actions CI | Auto-tests every pull request |
| Create 10 `good first issue` tickets | Invites new contributors in |
| Deploy to HuggingFace Spaces | Live demo anyone can try |
| Post on Reddit & communities | Gets the first wave of stars |

---

## 🗂️ Files to Create in This Phase

```
promptlens/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── new_connector.md     ← Custom template for adding models
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── ci.yml               ← GitHub Actions
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                      ← MIT License
└── README.md                    ← The polished final version
```

---

## ✍️ README Must-Haves

Your main README should have:

- [ ] **Project title + one-line description**
- [ ] **Demo GIF** (record with ShareX or Loom, convert to GIF)
- [ ] **Why PromptLens** — the problem it solves
- [ ] **Quick Start** — 3 commands to get running
- [ ] **Features list**
- [ ] **Screenshots**
- [ ] **How to contribute** (link to CONTRIBUTING.md)
- [ ] **Roadmap** (link to GitHub Projects)
- [ ] **License badge**

---

## ⚙️ GitHub Actions CI

Auto-runs on every PR to check:
- Python linting (flake8)
- Unit tests pass
- No broken imports

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: { python-version: '3.10' }
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/
```

---

## 🌍 Deploy to HuggingFace Spaces

HuggingFace Spaces gives you a free live demo link to share:

```bash
# Install HF CLI
pip install huggingface_hub

# Create a Space (Gradio or static)
huggingface-cli repo create promptlens --type space
```

---

## 📣 Where to Share

| Platform | What to Post |
|---|---|
| **Reddit r/MachineLearning** | Technical post about the eval approach |
| **Reddit r/Python** | Post about the open source project |
| **Reddit r/opensource** | General launch post |
| **LinkedIn** | Personal post as a final year project |
| **HuggingFace Discord** | Share in #projects channel |
| **Dev.to** | Write a blog post about building it |

---

## 🏷️ Good First Issues to Create

Create these as GitHub Issues labeled `good first issue` + `help wanted`:

1. Add toxicity metric using Detoxify library
2. Add Mistral API connector
3. Add Cohere API connector
4. Add CSV export for results
5. Add dark mode toggle
6. Write unit tests for readability metric
7. Add Hindi language support for sentiment metric
8. Add keyboard shortcut (Ctrl+Enter) to run
9. Add response word count to results table
10. Create a Docker setup for easy deployment

---

## ✅ Phase 4 Checklist

- [ ] README has demo GIF
- [ ] CONTRIBUTING.md is clear and friendly
- [ ] GitHub Actions CI is green
- [ ] 10 `good first issue` tickets created
- [ ] HuggingFace Space is live
- [ ] Posted to at least 2 communities
- [ ] First external contributor welcomed 🎉

---

## ⬅️ Prev: [Phase 3 — Web UI](../phase-3/README.md)

---

> 🎓 By the end of this phase, you have a real open source project on your resume, GitHub profile, and potentially your first contributors from the community.
