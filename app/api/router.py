from fastapi import APIRouter
from app.api import chat, embed

api_router = APIRouter()
api_router.include_router(embed.router, prefix="/api", tags=["Embedding"])
api_router.include_router(chat.router, prefix="/api", tags=["Chat"])
