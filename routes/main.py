from fastapi import APIRouter

from routes.alumnos import alumnos
from routes.grupos import grupos

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
api_router.include_router(grupos.router, prefix="/grupos", tags=["grupos"])
