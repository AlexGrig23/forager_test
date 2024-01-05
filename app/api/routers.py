"""API Routers."""
from fastapi import APIRouter

from app.api import email as email_routes
from app.api import phone as user_routes

api_router = APIRouter()

api_router.include_router(email_routes.router, prefix='/api/v1')
api_router.include_router(user_routes.router, prefix='/api/v1')
