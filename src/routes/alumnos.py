from fastapi import APIRouter, status

from src.dependencies.sqlmodel import SessionDep
from src.dependencies.database import DBAlumnosDep, DBGruposDep
from src.models.alumno import AlumnoUpsert
from src.models.error import Error
from src.models.public import AlumnoPublic, AlumnoPublicWithRelations

router = APIRouter()


@router.get("/")
def list(db: DBAlumnosDep, session: SessionDep) -> list[AlumnoPublic]:
    return db.list(session)


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(
    db: DBAlumnosDep, session: SessionDep, padron: int
) -> AlumnoPublicWithRelations:
    return db.find(session, padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    db: DBAlumnosDep, session: SessionDep, alumno_a_crear: AlumnoUpsert
) -> AlumnoPublic:
    alumno = db.add(session, alumno_a_crear)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(
    db: DBAlumnosDep, session: SessionDep, padron: int, alumno_actualizado: AlumnoUpsert
) -> AlumnoPublic:
    alumno = db.update(session, padron, alumno_actualizado)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(db: DBAlumnosDep, session: SessionDep, padron: int) -> AlumnoPublic:
    alumno = db.delete(session, padron)
    return alumno


@router.post("/{padron}/inscribirse/{grupo_id}", status_code=status.HTTP_201_CREATED)
def inscribirse(
    db_alumnos: DBAlumnosDep,
    db_grupos: DBGruposDep,
    session: SessionDep,
    grupo_id: int,
    padron: int,
) -> AlumnoPublicWithRelations:
    grupo = db_grupos.find(session, grupo_id)
    return db_alumnos.inscribirse_a_grupo(session, padron, grupo)
