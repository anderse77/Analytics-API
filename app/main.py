from fastapi import FastAPI
from .routers import health, items

app = FastAPI(title="Analytics API", version="0.1.0")
app.inlcude_router(health.router, prefix="/health", tags=["health"])
app.inlcude_router(items.router, prefix="/items", tags=["items"])