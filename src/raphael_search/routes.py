"""API routes for raphael-search."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(tags=["raphael-search"])


@router.get("")
def list_root() -> dict[str, str]:
  return {"service": "raphael-search", "status": "stub"}
