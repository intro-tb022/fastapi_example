from fastapi import HTTPException, status
from sqlmodel import select

from database import SessionDep
from models.alumno import Alumno
from models.grupo import Grupo
from models.materia import Materia
from models.public import AlumnoPublic, GrupoPublic, MateriaPublic

def buscar_alumno(session: SessionDep, padron: int) -> AlumnoPublic:
    alumno = session.exec(select(Alumno).where(
        Alumno.padron == padron)).first()

    if alumno:
        return alumno
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Alumno not found")

def buscar_grupo(session: SessionDep, grupo_id: int) -> GrupoPublic:
    query = select(Grupo).where(Grupo.id == grupo_id)
    grupo = session.exec(query).first()

    if grupo:
        return grupo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Grupo not found")

def buscar_materia(session: SessionDep, id: int) -> MateriaPublic:
    materia = session.exec(select(Materia).where(Materia.id == id)).first()

    if materia:
        return materia
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Materia not found")
