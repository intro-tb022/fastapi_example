from fastapi import APIRouter

from src.routes import grupos
from src.routes import alumnos
from src.routes import integrantes

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
api_router.include_router(grupos.router, prefix="/grupos", tags=["grupos"])
api_router.include_router(
    integrantes.router, prefix="/integrantes", tags=["integrantes"]
)
