from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from models import Alumno, AlumnoCreate, AlumnoPublic, Error
from database import SessionDep
from routes.grupos import grupos

router = APIRouter()


@router.get("/")
def list(session: SessionDep) -> list[Alumno]:
    query = select(Alumno)
    alumnos = session.exec(query)
    return alumnos

@router.get("/{padron}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, padron: int) -> AlumnoPublic:
    return buscar_alumno(session, padron)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, alumno_a_crear: AlumnoCreate) -> Alumno:
    alumno = Alumno(
        nombre=alumno_a_crear.nombre,
        apellido=alumno_a_crear.apellido,
        edad=alumno_a_crear.edad,
    )
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

@router.post("/{padron}/asignar_grupo")
def asignar_grupo(session: SessionDep, padron: int, grupo_id: int) -> Alumno:
    alumno = buscar_alumno(session, padron)
    grupo = grupos.buscar_grupo(session, grupo_id)

    alumno.grupo = grupo
    session.commit()
    session.refresh(alumno)
    return alumno


def buscar_alumno(session: SessionDep, padron: int) -> Alumno:
    alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

    if alumno:
        return alumno
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")
