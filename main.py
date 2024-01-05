"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.routers import api_router

app = FastAPI(title='Forager-test', openapi_url='/api/v1/openapi.json')

app.include_router(api_router)
