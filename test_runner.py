from backend.runner import run_evaluation

prompt = "Explain what a black hole is in simple terms"
models = ["qwen-7b"]
metrics = ["length", "readability", "sentiment"]

results = run_evaluation(prompt, models, metrics)

for r in results:
    print(f"\n✅ Model: {r['model']}")
    print(f"📝 Response: {r['response'][:120]}...")
    print(f"📊 Scores: {r['scores']}")