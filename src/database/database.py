from fastapi import HTTPException, status
from sqlmodel import select

from src.dependencies.sqlmodel import SessionDep
from src.models.alumno import Alumno, AlumnoUpsert

class Database:
    def __init__(self):
        self.alumnos = []

    def cargar_alumnos(self, alumnos: list[Alumno]):
        pass
    
    def list(self, session: SessionDep) -> list[Alumno]:
        query = select(Alumno)
        alumnos = session.exec(query)
        return alumnos
    
    def add(self, session: SessionDep, alumno_a_crear: AlumnoUpsert) -> Alumno:
        alumno = Alumno(**alumno_a_crear.model_dump())
        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def find(self, session: SessionDep, padron) -> Alumno:
        alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).one()

        if alumno:
            return alumno
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")
            
    def delete(self, session: SessionDep, padron) -> Alumno:
        alumno = self.find(padron)
        session.delete(alumno)
        session.commit()
        return alumno
    
    def update(self, session: SessionDep, padron, nuevo_alumno: AlumnoUpsert) -> Alumno:
        alumno = self.find(padron)
        alumno.nombre = nuevo_alumno.nombre
        alumno.apellido = nuevo_alumno.apellido
        alumno.edad = nuevo_alumno.edad

        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno
