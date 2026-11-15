from fastapi import FastAPI, APIRouter

from rag_pipeline import get_rag_pipeline
app = FastAPI(title="RAG App")
retriever, qa_chain = get_rag_pipeline()
router = APIRouter()

@app.get("/answer/")
def get_answer(question: str):
    response = qa_chain({"query": question})
    return response["result"]

# Run below command to start the server
# uvicorn main:app --reload --port 8000