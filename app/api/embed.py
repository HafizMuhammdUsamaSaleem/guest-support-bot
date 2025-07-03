from fastapi import APIRouter
from app.core.retriever import create_embeddings

router = APIRouter()

@router.post("/embed")
async def embed_faqs():
    create_embeddings()
    return {"message": "Embeddings created successfully."}
