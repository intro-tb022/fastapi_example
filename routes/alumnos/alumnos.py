from models import Alumno, AlumnoCreate, Error
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from models import Alumno, AlumnoCreate, Error
from database import SessionDep

router = APIRouter()


@router.get("/")
def list(session: SessionDep) -> list[Alumno]:
    query = select(Alumno)
    alumnos = session.exec(query)
    return alumnos

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, padron: int) -> Alumno:
    return buscar_alumno(session, padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, alumno_a_crear: AlumnoCreate) -> Alumno:
    alumno = Alumno(**alumno_a_crear.model_dump())
    session.add(alumno)
    session.commit()
    session.refresh(alumno)
    return alumno

@router.put("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(session: SessionDep, padron: int, alumno_actualizado: Alumno) -> Alumno:
    alumno = buscar_alumno(session, padron)
    alumno.nombre = alumno_actualizado.nombre
    alumno.apellido = alumno_actualizado.apellido
    alumno.edad = alumno_actualizado.edad
    session.add(alumno)
    session.commit()
    session.refresh(alumno)
    return alumno

@router.delete("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(session: SessionDep, padron: int) -> Alumno:
    alumno = buscar_alumno(session, padron)
    session.delete(alumno)
    session.commit()
    return alumno

@router.put("/{padron}/cargar_nota")
def cargar_nota(padron: int, nota: int) -> Alumno:
    alumno = buscar_alumno(padron)
    alumno.notas.append(nota)
    return alumno


def buscar_alumno(session: SessionDep, padron: int) -> Alumno:
    alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).one()

    if alumno:
        return alumno
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")
