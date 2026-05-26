async function runEvaluation() {
  const prompt = document.getElementById("prompt").value.trim();
  if (!prompt) {
    alert("Please enter a prompt!");
    return;
  }

  // Get selected models
  const modelBoxes = document.querySelectorAll(
    ".checkbox-group input[type=checkbox]",
  );
  const models = [];
  const metrics = [];

  document
    .querySelectorAll(".card:nth-child(2) input:checked")
    .forEach((cb) => models.push(cb.value));
  document
    .querySelectorAll(".card:nth-child(3) input:checked")
    .forEach((cb) => metrics.push(cb.value));

  if (models.length === 0) {
    alert("Select at least one model!");
    return;
  }
  if (metrics.length === 0) {
    alert("Select at least one metric!");
    return;
  }

  // Show loading
  document.getElementById("runBtn").disabled = true;
  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("results").innerHTML = "";

  try {
    const res = await fetch("http://localhost:8000/evaluate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, models, metrics }),
    });

    const data = await res.json();
    renderResults(data.results);
  } catch (err) {
    document.getElementById("results").innerHTML =
      `<p style="color:#ef5350; text-align:center;">
        ❌ Could not connect to backend. Make sure the server is running at localhost:8000
      </p>`;
  } finally {
    document.getElementById("runBtn").disabled = false;
    document.getElementById("loading").classList.add("hidden");
  }
}

function renderResults(results) {
  const container = document.getElementById("results");
  if (!results || results.length === 0) {
    container.innerHTML =
      '<p style="color:#aaa;text-align:center;">No results returned.</p>';
    return;
  }

  const grid = document.createElement("div");
  grid.className = "results-grid";

  results.forEach((r) => {
    const card = document.createElement("div");
    card.className = "result-card";

    const copyId = `resp-${r.model}`;

    card.innerHTML = `
      <h3>
        🤖 ${r.model}
        <button class="copy-btn" onclick="copyText('${copyId}')">Copy</button>
      </h3>
      <div class="response-text" id="${copyId}">${r.response}</div>
      <div class="scores">${renderScores(r.scores)}</div>
    `;

    grid.appendChild(card);
  });

  container.appendChild(grid);
}

function renderScores(scores) {
  let html = "";

  if (scores.length) {
    html += `<div class="score-row">
      <label>sentiment</label>
      <span class="sentiment-badge ${scores.sentiment.label}">
        ${scores.sentiment.label} (${scores.sentiment.score})
      </span>
    </div>`;
  }

  if (scores.length) {
    const ease = scores.readability?.flesch_reading_ease ?? 0;
    const pct = Math.min(Math.max(ease, 0), 100);
    html += `<div class="score-row">
      <label>readability — Flesch ease ${ease.toFixed(1)}</label>
      <div class="score-bar-wrap"><div class="score-bar" style="width:${pct}%"></div></div>
      <div class="score-value">Grade level: ${scores.readability?.grade_level?.toFixed(1) ?? "N/A"}</div>
    </div>`;
  }

  if (scores.length) {
    const words = scores.length?.words ?? 0;
    const pct = Math.min((words / 300) * 100, 100);
    html += `<div class="score-row">
      <label>length — ${words} words / ${scores.length?.chars ?? 0} chars</label>
      <div class="score-bar-wrap"><div class="score-bar" style="width:${pct}%"></div></div>
    </div>`;
  }

  // Generic fallback for any score
  if (!html) {
    for (const [key, val] of Object.entries(scores)) {
      html += `<div class="score-row">
        <label>${key}</label>
        <div class="score-value">${JSON.stringify(val)}</div>
      </div>`;
    }
  }

  return html;
}

function copyText(id) {
  const text = document.getElementById(id)?.innerText;
  if (text) {
    navigator.clipboard.writeText(text);
    alert("Copied!");
  }
}

// Allow Ctrl+Enter to run while typing inside the prompt box
const promptInput = document.getElementById("prompt");
if (promptInput) {
  promptInput.addEventListener("keydown", (e) => {
    // Check if the user presses Enter while holding down the Ctrl key
    if (e.ctrlKey && e.key === "Enter") {
      e.preventDefault(); // Stop a new line from being added in the textarea
      // Trigger the evaluation directly
      runEvaluation();
    } 
  });
}

const THEME_KEY = "promptlens-theme";

function setTheme(theme) {
  const body = document.body;
  const isLight = theme === "light";
  body.classList.toggle("light-theme", isLight);
  body.setAttribute("data-theme", theme);

  const toggle = document.getElementById("themeToggle");
  if (toggle) {
    toggle.textContent = isLight ? "🌙 Dark" : "☀️ Light";
    toggle.setAttribute(
      "aria-label",
      `Switch to ${isLight ? "dark" : "light"} theme`,
    );
  }

  localStorage.setItem(THEME_KEY, theme);
}

function toggleTheme() {
  setTheme(document.body.classList.contains("light-theme") ? "dark" : "light");
}

function initTheme() {
  const saved = localStorage.getItem(THEME_KEY);
  const defaultTheme =
    saved === "light" || saved === "dark"
      ? saved
      : window.matchMedia?.("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
  setTheme(defaultTheme);
}

initTheme();

const themeToggle = document.getElementById("themeToggle");
if (themeToggle) {
  themeToggle.addEventListener("click", toggleTheme);
}
