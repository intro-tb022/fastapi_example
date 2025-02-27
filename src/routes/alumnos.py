from fastapi import APIRouter, status

from src.models import Alumno, AlumnoUpsert, Error
from src.dependencies import RepositoryDep

router = APIRouter()

@router.get("/")
def list(repo: RepositoryDep) -> list[Alumno]:
    return repo.list()

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(repo: RepositoryDep, padron: int) -> Alumno:
    return repo.find(padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(repo: RepositoryDep, alumno_a_crear: AlumnoUpsert) -> Alumno:
    alumno = repo.add(alumno_a_crear)
    return alumno

@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(repo: RepositoryDep, padron: int, alumno_actualizado: AlumnoUpsert) -> Alumno:
    alumno = repo.update(padron, alumno_actualizado)
    return alumno

@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(repo: RepositoryDep, padron: int) -> Alumno:
    alumno = repo.delete(padron)
    return alumno

@router.put("/{padron}/cargar_nota", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def cargar_nota(repo: RepositoryDep, padron: int, nota: int) -> Alumno:
    alumno = repo.cargar_nota(padron, nota)
    return alumno

