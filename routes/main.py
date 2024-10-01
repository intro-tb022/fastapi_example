from fastapi import APIRouter

from routes.alumnos import alumnos
from routes.grupos import grupos
from routes.materias import materias

api_router = APIRouter()
api_router.include_router(alumnos.router, prefix="/alumnos", tags=["alumnos"])
api_router.include_router(grupos.router, prefix="/grupos", tags=["grupos"])
api_router.include_router(materias.router, prefix="/materias", tags=["materias"])