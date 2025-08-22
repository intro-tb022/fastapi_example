from typing import Annotated

from fastapi import APIRouter, Query, status

from dependencies.database import DBAlumnosDep
from dependencies.sqlmodel import SessionDep
from models.alumno import AlumnoUpsert, FiltrosAlumno
from models.error import Error
from models.public import AlumnoPublic, AlumnoPublicWithRelations

router = APIRouter()


@router.get("/")
def list(
    session: SessionDep,
    db: DBAlumnosDep,
    filtros: Annotated[FiltrosAlumno, Query()],
) -> list[AlumnoPublic]:
    return db.list(session, filtros)


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, db: DBAlumnosDep, padron: int) -> AlumnoPublicWithRelations:
    return db.find(session, padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, db: DBAlumnosDep, alumno_a_crear: AlumnoUpsert) -> AlumnoPublic:
    alumno = db.add(session, alumno_a_crear)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(session: SessionDep, db: DBAlumnosDep, padron: int, alumno_actualizado: AlumnoUpsert) -> AlumnoPublic:
    alumno = db.update(session, padron, alumno_actualizado)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(session: SessionDep, db: DBAlumnosDep, padron: int) -> AlumnoPublic:
    alumno = db.delete(session, padron)
    return alumno
