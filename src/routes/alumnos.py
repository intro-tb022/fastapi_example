from fastapi import APIRouter, status

from src.dependencies.database import DBAlumnosDep, DBGruposDep
from src.models.alumno import AlumnoUpsert
from src.models.error import Error
from src.models.public import AlumnoPublic, AlumnoPublicWithRelations

router = APIRouter()


@router.get("/")
def list(db: DBAlumnosDep) -> list[AlumnoPublic]:
    return db.list()


@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DBAlumnosDep, padron: int) -> AlumnoPublicWithRelations:
    return db.find(padron)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(db: DBAlumnosDep, alumno_a_crear: AlumnoUpsert) -> AlumnoPublic:
    alumno = db.add(alumno_a_crear)
    return alumno


@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(
    db: DBAlumnosDep, padron: int, alumno_actualizado: AlumnoUpsert
) -> AlumnoPublic:
    alumno = db.update(padron, alumno_actualizado)
    return alumno


@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(db: DBAlumnosDep, padron: int) -> AlumnoPublic:
    alumno = db.delete(padron)
    return alumno


@router.put("/{padron}/asignar_grupo", status_code=status.HTTP_200_OK)
def asignar_grupo(
    db_alumnos: DBAlumnosDep,
    db_grupos: DBGruposDep,
    padron: int,
    grupo_id: int,
) -> AlumnoPublicWithRelations:
    grupo = db_grupos.find(grupo_id)
    return db_alumnos.inscribirse_a_grupo(padron, grupo)
