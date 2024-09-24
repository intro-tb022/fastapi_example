from fastapi import APIRouter

from routes.alumnos import alumnos

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
