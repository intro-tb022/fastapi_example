from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.alumno import Alumno, AlumnoUpsert

class Database:
    def __init__(self, engine):
        self.engine = engine

    def session(self):
        with Session(self.engine) as session:
            return session

    def cargar_alumnos(self, alumnos: list[Alumno]):
        session = self.session()
        session.add_all(alumnos)
        session.commit()
    
    def list(self) -> list[Alumno]:
        with self.session() as session:
            query = select(Alumno)
            alumnos = session.exec(query).all()
            return alumnos
    
    def add(self, alumno_a_crear: AlumnoUpsert) -> Alumno:
        with Session(self.engine) as session:
            alumno = Alumno(**alumno_a_crear.model_dump())
            session.add(alumno)
            session.commit()
            session.refresh(alumno)
            return alumno

    def find(self, padron: int) -> Alumno:
        with Session(self.engine) as session:
            alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

            if alumno:
                return alumno
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")
            
    def delete(self, padron: int) -> Alumno:
        with Session(self.engine) as session:
            alumno = self.find(padron)
            session.delete(alumno)
            session.commit()
            return alumno
    
    def update(self, padron: int, nuevo_alumno: AlumnoUpsert) -> Alumno:
        with Session(self.engine) as session:
            alumno = self.find(padron)
            alumno.nombre = nuevo_alumno.nombre
            alumno.apellido = nuevo_alumno.apellido
            alumno.edad = nuevo_alumno.edad

            session.add(alumno)
            session.commit()
            session.refresh(alumno)
            return alumno
