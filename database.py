from collections.abc import Generator
import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemyseeder import ResolvingSeeder
from sqlmodel import create_engine, select, Session

from models.alumno import Alumno

SQLITE_FILE_PATH = "database.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]

logger = logging.getLogger(__name__)

def seed():
    with Session(engine) as session:
        # Do no seed if there's data present in the DB
        if session.exec(select(Alumno)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        alumnos = [
            Alumno(padron=94557, nombre="Federico", apellido="Esteban", edad=31),
            Alumno(padron=95557, nombre="Daniela", apellido="Riesgo", edad=30),
            Alumno(padron=99779, nombre="Juan Ignacio", apellido="Kristal", edad=27),
        ]

        session.add_all(alumnos)

        session.commit()

        logger.info("Seeds loaded on Db")
