from fastapi import APIRouter, status

from models.alumno import Alumno, AlumnoUpsert, Error
from dependencies.database import DatabaseDep

router = APIRouter()

@router.get("/")
def list(db: DatabaseDep) -> list[Alumno]:
    return db.list()

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(db: DatabaseDep, padron: int) -> Alumno:
    return db.find(padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(db: DatabaseDep, alumno_a_crear: AlumnoUpsert) -> Alumno:
    alumno = db.add(alumno_a_crear)
    return alumno

@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(db: DatabaseDep, padron: int, alumno_actualizado: AlumnoUpsert) -> Alumno:
    alumno = db.update(padron, alumno_actualizado)
    return alumno

@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(db: DatabaseDep, padron: int) -> Alumno:
    alumno = db.delete(padron)
    return alumno

@router.put("/{padron}/cargar_nota", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def cargar_nota(db: DatabaseDep, padron: int, nota: int) -> Alumno:
    alumno = db.cargar_nota(padron, nota)
    return alumno

