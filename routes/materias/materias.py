import logging

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from models.materia import Materia, MateriaCreate
from models.error import Error
from models.public import MateriaPublic, MateriaPublicWithAlumnos
from database import SessionDep
import routes.utils as utils

router = APIRouter()

@router.get("/")
def list(session: SessionDep) -> list[MateriaPublic]:
    query = select(Materia)
    materias = session.exec(query)
    return materias

@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, id: int) -> MateriaPublicWithAlumnos:
    return utils.buscar_materia(session, id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(session: SessionDep, materia_a_crear: MateriaCreate) -> MateriaPublic:
    materia = Materia(
        nombre=materia_a_crear.nombre,
    )
    session.add(materia)
    session.commit()
    session.refresh(materia)

    return materia

@router.delete("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def delete(session: SessionDep, id: int) -> MateriaPublic:
    materia = utils.buscar_materia(session, id)
    session.delete(materia)
    session.commit()

    return materia


@router.post("/{id}/inscribir_alumno", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def inscribir_alumno(session: SessionDep, id: int, padron: int) -> MateriaPublicWithAlumnos:
    materia = utils.buscar_materia(session, id)
    alumno = utils.buscar_alumno(session, padron)

    materia.alumnos.append(alumno)
    session.add(materia)
    session.commit()

    return materia


@router.post("/{id}/desinscribir_alumno", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def desinscribir_alumno(session: SessionDep, id: int, padron: int) -> MateriaPublicWithAlumnos:
    materia = utils.buscar_materia(session, id)
    alumno = utils.buscar_alumno(session, padron)

    materia.alumnos.remove(alumno)
    session.add(materia)
    session.commit()

    return materia
