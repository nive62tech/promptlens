import importlib, os, sys

print("\n===== PROMPTLENS STATUS CHECK =====\n")

# Check folder structure
folders = [
    "backend", "backend/connectors", "backend/metrics",
    "phase-1", "phase-2", "phase-3", "phase-4"
]
print("📁 FOLDER STRUCTURE:")
for f in folders:
    status = "✅" if os.path.isdir(f) else "❌"
    print(f"  {status} {f}/")

# Check files
files = [
    "backend/__init__.py", "backend/runner.py",
    "backend/connectors/__init__.py",
    "backend/connectors/gemini_connector.py",
    "backend/connectors/hf_connector.py",
    "backend/metrics/__init__.py",
    "backend/metrics/length.py",
    "backend/metrics/readability.py",
    "backend/metrics/sentiment.py",
    "requirements.txt", ".env", ".env.example",
    "test_runner.py"
]
print("\n📄 FILES:")
for f in files:
    status = "✅" if os.path.isfile(f) else "❌"
    print(f"  {status} {f}")

# Check packages
print("\n📦 PACKAGES:")
packages = ["dotenv", "openai", "google.genai", "huggingface_hub", "textstat", "textblob", "requests", "fastapi", "uvicorn"]
for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"  ✅ {pkg}")
    except:
        print(f"  ❌ {pkg} — not installed")

# Check .env keys
print("\n🔑 API KEYS:")
from dotenv import load_dotenv
load_dotenv()
keys = ["OPENAI_API_KEY", "GEMINI_API_KEY", "HF_API_KEY"]
for k in keys:
    val = os.getenv(k)
    if val and "your_" not in val and len(val) > 5:
        print(f"  ✅ {k} — set")
    else:
        print(f"  ❌ {k} — missing or placeholder")

print("\n===================================\n")