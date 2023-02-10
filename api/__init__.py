"""Routes principal"""
from fastapi import APIRouter
from .routes import routes

api_router_main = APIRouter()

api_router_main.include_router(
    routes.mi_api_router
)
