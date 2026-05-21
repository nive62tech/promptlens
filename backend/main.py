from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.models.schemas import EvaluateRequest, EvaluateResponse
from backend.runner import run_evaluation
import os

app = FastAPI(
    title="PromptLens API",
    description="Local-first prompt evaluation toolkit",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "message": "PromptLens is running"}

@app.get("/models")
def list_models():
    return {"models": ["gemini-pro", "qwen-7b"]}

@app.get("/metrics")
def list_metrics():
    return {"metrics": ["length", "readability", "sentiment"]}

@app.post("/evaluate", response_model=EvaluateResponse)
def evaluate(request: EvaluateRequest):
    results = run_evaluation(request.prompt, request.models, request.metrics)
    return EvaluateResponse(prompt=request.prompt, results=results)

# Serve frontend — must be last
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")