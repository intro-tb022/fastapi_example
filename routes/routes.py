from fastapi import APIRouter

from routes import alumnos, grupos, integrantes

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
api_router.include_router(grupos.router, prefix="/grupos", tags=["grupos"])
api_router.include_router(integrantes.router, prefix="/integrantes", tags=["integrantes"])
