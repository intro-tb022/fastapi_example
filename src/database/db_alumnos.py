from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.alumno import Alumno, AlumnoUpsert
from src.models.integrante import Integrante


class DBAlumnos:
    def cargar_alumnos(self, session: Session, alumnos: list[Alumno]):
        session.add_all(alumnos)
        session.commit()

    def list(self, session: Session) -> list[Alumno]:
        query = select(Alumno)
        alumnos = session.exec(query).all()
        return alumnos

    def add(self, session: Session, alumno_a_crear: AlumnoUpsert) -> Alumno:
        alumno = Alumno(**alumno_a_crear.model_dump())
        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def find(self, session: Session, padron: int) -> Alumno:
        return self.__get(session, padron)

    def delete(self, session: Session, padron: int) -> Alumno:
        alumno = self.__get(session, padron)
        session.delete(alumno)
        session.commit()
        return alumno

    def update(self, session: Session, padron: int, nuevo_alumno: AlumnoUpsert) -> Alumno:
        alumno = self.__get(session, padron)
        update_dict = nuevo_alumno.model_dump(exclude_unset=True)
        alumno.sqlmodel_update(update_dict)

        session.add(alumno)
        session.commit()
        session.refresh(alumno)
        return alumno

    def inscribirse_a_grupo(self, session: Session, padron: int, grupo_id: int) -> Alumno:
        alumno = self.__get(session, padron)
        integrante = Integrante(grupo_id=grupo_id, alumno_padron=padron)
        session.add(integrante)
        session.commit()
        session.refresh(alumno)
        return alumno

    def remover_de_grupo(self, session: Session, padron: int, grupo_id: int) -> Alumno:
        alumno = self.__get(session, padron)
        integrante = session.exec(
            select(Integrante).where(Integrante.alumno_padron == padron, Integrante.grupo_id == grupo_id)
        ).first()
        session.delete(integrante)
        session.commit()
        session.refresh(alumno)
        return alumno

    def __get(self, session: Session, padron: int) -> Alumno:
        alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

        if alumno:
            return alumno
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")
