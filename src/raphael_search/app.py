"""Raphael service: raphael-search."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from raphael_contracts.errors import ErrorResponse
from raphael_search.routes import router

app = FastAPI(
    title="raphael-search",
    description="Global and scoped search, semantic search",
    version="0.1.0",
    openapi_url="/v1/search/openapi.json" if "/v1/search" else "/openapi.json",
)

app.include_router(router, prefix="/v1/search" if "/v1/search" else "")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "raphael-search"}


@app.exception_handler(Exception)
async def unhandled(_request, exc: Exception) -> JSONResponse:
    err = ErrorResponse(code="internal_error", message=str(exc))
    return JSONResponse(status_code=500, content=err.model_dump())
