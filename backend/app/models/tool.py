from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class Tool(BaseModel):
    """Single developer utility entry."""

    id: str
    name: str
    description: str
    category: str
    tags: List[str]
    url: HttpUrl
    icon: Optional[HttpUrl] = None
    featured: bool = False


class ToolCategory(BaseModel):
    """Descriptor for tool group summaries."""

    id: str
    title: str
    description: str
    icon: Optional[str] = None
