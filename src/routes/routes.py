from fastapi import APIRouter

from src.routes import alumnos

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
