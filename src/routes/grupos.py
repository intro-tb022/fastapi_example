from fastapi import APIRouter, status

from src.models.public import GrupoPublic, GrupoPublicWithIntegrantes
from src.dependencies.database import DBGruposDep
from src.models.grupo import GrupoUpsert
from src.models.error import Error

router = APIRouter()


@router.get("/")
def list(db: DBGruposDep) -> list[GrupoPublic]:
    return db.list()


@router.get("/{grupo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DBGruposDep, grupo_id: int) -> GrupoPublicWithIntegrantes:
    return db.find(grupo_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(db: DBGruposDep, grupo_a_crear: GrupoUpsert) -> GrupoPublic:
    alumno = db.add(grupo_a_crear)
    return alumno
