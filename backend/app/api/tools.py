from __future__ import annotations

from typing import Annotated, List, Optional

from fastapi import APIRouter, Query

from app.data.tools import TOOL_CATEGORIES, TOOLS
from app.models.tool import Tool, ToolCategory

router = APIRouter(prefix="/tools", tags=["tools"])


@router.get("", response_model=List[Tool])
def list_tools(
    category: Optional[str] = Query(default=None, description="按分类过滤"),
    q: Annotated[
        Optional[str],
        Query(description="关键词匹配 name / description / tags"),
    ] = None,
    featured: bool | None = Query(
        default=None, description="仅返回精选工具"
    ),
) -> list[Tool]:
    items = TOOLS

    if category:
        items = [tool for tool in items if tool.category == category]

    if featured is not None:
        items = [tool for tool in items if tool.featured == featured]

    if q:
        q_lower = q.lower()
        items = [
            tool
            for tool in items
            if q_lower in tool.name.lower()
            or q_lower in tool.description.lower()
            or any(q_lower in tag.lower() for tag in tool.tags)
        ]

    return items


@router.get("/categories", response_model=List[ToolCategory])
def list_categories() -> list[ToolCategory]:
    return TOOL_CATEGORIES
