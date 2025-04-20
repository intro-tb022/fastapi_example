from fastapi import APIRouter, HTTPException, status

from dependencies.database import DBGruposDep
from dependencies.sqlmodel import SessionDep
from models.error import Error
from models.grupo import GrupoUpsert
from models.integrante import MAX_SIZE, IntegranteCreate
from models.public import GrupoPublic, GrupoPublicWithIntegrantes

router = APIRouter()


@router.get("/")
def list(session: SessionDep, db: DBGruposDep) -> list[GrupoPublic]:
    return db.list(session)


@router.get("/{grupo_id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, db: DBGruposDep, grupo_id: int) -> GrupoPublicWithIntegrantes:
    return db.find(session, grupo_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": Error}},
)
def create(session: SessionDep, db: DBGruposDep, grupo_a_crear: GrupoUpsert) -> GrupoPublicWithIntegrantes:
    if len(grupo_a_crear.integrantes) > MAX_SIZE:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Grupo admite hasta 4 integrantes",
        )
    grupo = db.add(session, grupo_a_crear)
    return grupo


@router.post("/{grupo_id}/integrantes", status_code=status.HTTP_201_CREATED)
def inscribir(
    session: SessionDep,
    db: DBGruposDep,
    grupo_id: int,
    integrante_nuevo: IntegranteCreate,
) -> GrupoPublicWithIntegrantes:
    return db.inscribir(session, grupo_id, integrante_nuevo)


@router.delete("/{grupo_id}/integrantes/{padron}")
def desinscribir(
    session: SessionDep,
    db: DBGruposDep,
    grupo_id: int,
    padron: int,
) -> GrupoPublicWithIntegrantes:
    return db.desinscribir(session, grupo_id, padron)
