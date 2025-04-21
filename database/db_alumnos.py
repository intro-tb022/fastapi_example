from fastapi import HTTPException, status
from sqlmodel import Session, select

from models.alumno import Alumno, AlumnoUpsert, FiltrosAlumno

default_limit = 10


class DBAlumnos:
    def cargar_alumnos(self, session: Session, alumnos: list[Alumno]):
        session.add_all(alumnos)
        session.commit()

    def list(self, session: Session, filters) -> list[Alumno]:
        query = self.__build_list_query(filters)
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

    def __get(self, session: Session, padron: int) -> Alumno:
        alumno = session.exec(select(Alumno).where(Alumno.padron == padron)).first()

        if alumno:
            return alumno
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno not found")

    def __build_list_query(self, filters: FiltrosAlumno):
        query = select(Alumno)
        if filters:
            for key, val in filters.model_dump(exclude=["limit", "offset"], exclude_none=True).items():
                if key in ["nombre", "apellido"]:
                    query = query.where(Alumno.nombre.like(f"%{val}%"))
                else:
                    query = query.where(getattr(Alumno, key) == val)

        query = query.limit(filters.limit).offset(filters.offset)
        return query
