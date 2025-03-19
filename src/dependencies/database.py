from typing import Annotated

from fastapi import Depends

from src.database.db_alumnos import DBAlumnos
from src.database.db_grupos import DBGrupos

__database_alumnos_instance = None
__database_grupos_instance = None


def init_db(engine):
    global __database_alumnos_instance
    global __database_grupos_instance
    __database_alumnos_instance = DBAlumnos(engine)
    __database_grupos_instance = DBGrupos(engine)


def get_db_alumnos() -> DBAlumnos:
    global __database_alumnos_instance
    if __database_alumnos_instance is None:
        raise RuntimeError("Database instance not initialized.")
    return __database_alumnos_instance


def get_db_grupos() -> DBGrupos:
    global __database_grupos_instance
    if __database_grupos_instance is None:
        raise RuntimeError("Database instance not initialized.")
    return __database_grupos_instance


DBAlumnosDep = Annotated[DBAlumnos, Depends(get_db_alumnos)]
DBGruposDep = Annotated[DBGrupos, Depends(get_db_grupos)]
