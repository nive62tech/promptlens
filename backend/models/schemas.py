from pydantic import BaseModel
from typing import List

class EvaluateRequest(BaseModel):
    prompt: str
    models: List[str]
    metrics: List[str]

class ModelResult(BaseModel):
    model: str
    response: str
    scores: dict

class EvaluateResponse(BaseModel):
    prompt: str
    results: List[ModelResult]