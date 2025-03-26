from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.integrante import Integrante
from src.models.grupo import Grupo
from src.models.alumno import Alumno, AlumnoUpsert


class DBAlumnos:
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
        session = self.session()
        query = select(Alumno)
        alumnos = session.exec(query).all()
        return alumnos

    def add(self, alumno_a_crear: AlumnoUpsert) -> Alumno:
        session = self.session()
        alumno = Alumno(**alumno_a_crear.model_dump())
        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def find(self, padron: int) -> Alumno:
        session = self.session()
        return self.__get(session, padron)

    def delete(self, padron: int) -> Alumno:
        session = self.session()
        alumno = self.__get(session, padron)
        session.delete(alumno)
        session.commit()
        return alumno

    def update(self, padron: int, nuevo_alumno: AlumnoUpsert) -> Alumno:
        session = self.session()
        alumno = self.__get(session, padron)
        update_dict = nuevo_alumno.model_dump(exclude_unset=True)
        alumno.sqlmodel_update(update_dict)

        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def inscribirse_a_grupo(self, padron: int, grupo: Grupo) -> Alumno:
        session = self.session()
        grupo = session.merge(grupo)
        alumno = self.__get(session, padron)
        integrante = Integrante(alumno=alumno, grupo=grupo)
        session.add(integrante)
        session.commit()
        session.refresh(alumno)
        return alumno

    def __get(self, session: Session, padron: int) -> Alumno:
        alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

        if alumno:
            return alumno
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found"
        )
