from typing import Annotated
from fastapi import APIRouter, Depends, status

from src.models import Alumno, AlumnoUpsert, Error
from src.repository.repository import Repository, repository

def get_repository() -> Repository:
   return repository


router = APIRouter()

@router.get("/")
def list() -> list[Alumno]:
    return get_repository().list()

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(padron: int) -> Alumno:
    return get_repository().find(padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(alumno_a_crear: AlumnoUpsert) -> Alumno:
    alumno = get_repository().add(alumno_a_crear)
    return alumno

@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(padron: int, alumno_actualizado: AlumnoUpsert) -> Alumno:
    alumno = get_repository().update(padron, alumno_actualizado)
    return alumno

@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(padron: int) -> Alumno:
    alumno = get_repository().delete(padron)
    return alumno

@router.put("/{padron}/cargar_nota", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def cargar_nota(padron: int, nota: int) -> Alumno:
    alumno = get_repository().cargar_nota(padron, nota)
    return alumno
