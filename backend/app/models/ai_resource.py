from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class AIResource(BaseModel):
    """Represents an AI model or platform landing entry."""

    id: str
    name: str
    provider: str
    category: str
    description: str
    docs_url: HttpUrl
    console_url: Optional[HttpUrl] = None
    tags: List[str] = []
    difficulty: str = "入门"
    highlight: bool = False
