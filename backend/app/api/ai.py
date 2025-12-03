from __future__ import annotations

from typing import Annotated, List, Optional

from fastapi import APIRouter, Query

from app.data.ai_resources import AI_RESOURCES
from app.models.ai_resource import AIResource

router = APIRouter(prefix="/ai", tags=["ai"])


@router.get("", response_model=List[AIResource])
def list_ai_resources(
    provider: Optional[str] = Query(default=None, description="按厂商筛选"),
    category: Optional[str] = Query(default=None, description="按类型筛选"),
    highlight: Annotated[
        Optional[bool], Query(description="只展示精选资源")
    ] = None,
    tag: Annotated[
        Optional[str], Query(description="标签匹配，如 多模态/低成本")
    ] = None,
    difficulty: Annotated[
        Optional[str], Query(description="入门/进阶/实验")
    ] = None,
) -> list[AIResource]:
    items = AI_RESOURCES

    if provider:
        items = [res for res in items if res.provider == provider]
    if category:
        items = [res for res in items if res.category == category]
    if highlight is not None:
        items = [res for res in items if res.highlight == highlight]
    if tag:
        tag_lower = tag.lower()
        items = [
            res for res in items if any(tag_lower in t.lower() for t in res.tags)
        ]
    if difficulty:
        items = [res for res in items if res.difficulty == difficulty]
    return items
