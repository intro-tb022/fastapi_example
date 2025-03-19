from fastapi import APIRouter, status

from src.dependencies.sqlmodel import SessionDep
from src.models.public import GrupoPublic, GrupoPublicWithIntegrantes
from src.dependencies.database import DBAlumnosDep, DBGruposDep
from src.models.grupo import Grupo, GrupoUpsert
from src.models.error import Error

router = APIRouter()


@router.get("/")
def list(db: DBGruposDep, session: SessionDep) -> list[GrupoPublic]:
    return db.list(session)


@router.get("/{grupo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(
    db: DBGruposDep, session: SessionDep, grupo_id: int
) -> GrupoPublicWithIntegrantes:
    return db.find(session, grupo_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    db: DBGruposDep, session: SessionDep, grupo_a_crear: GrupoUpsert
) -> GrupoPublic:
    alumno = db.add(session, grupo_a_crear)
    return alumno
