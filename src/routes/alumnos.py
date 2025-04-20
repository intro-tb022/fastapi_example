from fastapi import APIRouter, status

from src.dependencies.database import DBAlumnosDep
from src.dependencies.sqlmodel import SessionDep
from src.models.alumno import AlumnoUpsert
from src.models.error import Error
from src.models.public import AlumnoPublic, AlumnoPublicWithRelations

router = APIRouter()


@router.get("/")
def list(session: SessionDep, db: DBAlumnosDep) -> list[AlumnoPublic]:
    return db.list(session)


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


@router.put("/{padron}/asignar_grupo")
def asignar_grupo(
    session: SessionDep,
    db_alumnos: DBAlumnosDep,
    padron: int,
    grupo_id: int,
) -> AlumnoPublicWithRelations:
    return db_alumnos.inscribirse_a_grupo(session, padron, grupo_id)


@router.put("/{padron}/remover_grupo")
def remover_grupo(
    session: SessionDep,
    db_alumnos: DBAlumnosDep,
    padron: int,
    grupo_id: int,
) -> AlumnoPublicWithRelations:
    return db_alumnos.remover_de_grupo(session, padron, grupo_id)
