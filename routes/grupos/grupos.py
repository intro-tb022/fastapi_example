from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from database import SessionDep
from models import Grupo, GrupoPublic, Error

router = APIRouter()


@router.get("/")
def list(session: SessionDep) -> list[Grupo]:
    query = select(Grupo)
    grupos = session.exec(query)
    return grupos

@router.get("/{grupo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, grupo_id: int) -> GrupoPublic:
    return buscar_grupo(session, grupo_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, grupo: Grupo) -> Grupo:
    session.add(grupo)
    session.commit()
    session.refresh(grupo)
    return grupo

def buscar_grupo(session: SessionDep, grupo_id: int) -> Grupo:
    query = select(Grupo).where(Grupo.id == grupo_id)
    grupo = session.exec(query).first()

    if grupo:
        return grupo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Grupo not found")
