from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MistakeTutor API", version="0.0.1")

class AnalyzeRequest(BaseModel):
    problem: str
    student_answer: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    return {
        "mistake_type": "demo-błąd",
        "confidence": 0.6,
        "category": "demo",
        "diagnosis": "To jest odpowiedź demo z backendu. Backend działa poprawnie.",
        "key_concept": "demo-koncepcja",
        "micro_lesson": "Tutaj później podepniemy prawdziwą analizę AI.",
        "pitfalls": ["demo 1", "demo 2", "demo 3"],
        "next_steps": ["demo krok 1", "demo krok 2", "demo krok 3"],
    }
