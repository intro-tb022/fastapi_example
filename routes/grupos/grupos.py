from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from database import SessionDep
from models.grupo import Grupo
from models.public import GrupoPublic, GrupoPublicWithAlumnos
from models.error import Error
import routes.utils as utils

router = APIRouter()


@router.get("/")
def list(session: SessionDep) -> list[GrupoPublic]:
    query = select(Grupo)
    grupos = session.exec(query)
    return grupos

@router.get("/{grupo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, grupo_id: int) -> GrupoPublicWithAlumnos:
    return utils.buscar_grupo(session, grupo_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, grupo: Grupo) -> GrupoPublic:
    session.add(grupo)
    session.commit()
    session.refresh(grupo)
    return grupo

