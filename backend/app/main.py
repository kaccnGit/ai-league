from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import ai, health, tools, utils

app = FastAPI(
    title="AI League 工具站",
    description="开发者常用工具与 AI 资源聚合 API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(tools.router, prefix="/api")
app.include_router(ai.router, prefix="/api")
app.include_router(utils.router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AI League API ready"}
