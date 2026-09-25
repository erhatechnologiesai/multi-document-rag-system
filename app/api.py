from fastapi import FastAPI
from app.config import settings
from app.models import MultiDocQuery
from app.services.multi_doc_engine import search_corpus, CORPUS

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/documents")
def list_documents():
    return {"total": len(CORPUS), "documents": [{"name": d["name"], "type": d["type"]} for d in CORPUS]}

@app.post("/query")
def query_multi_doc(req: MultiDocQuery):
    results = search_corpus(req.question, req.filter_type)
    best = results[0]
    return {
        "question": req.question,
        "answer": f"According to {best['name']}: {best['text']}",
        "matched_documents": [d["name"] for d in results]
    }
