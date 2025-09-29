from fastapi import FastAPI
from .routers import health, items

app = FastAPI(title="Analytics API", version="0.1.0")
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(items.router, prefix="/items", tags=["items"])
