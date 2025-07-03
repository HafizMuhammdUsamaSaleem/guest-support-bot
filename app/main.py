from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Guest Support Concierge Bot",
)

app.include_router(api_router)
