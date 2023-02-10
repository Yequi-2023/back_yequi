"""Creacion FastApi"""
from api import api_router_main
from core.config import application

application.include_router(api_router_main)