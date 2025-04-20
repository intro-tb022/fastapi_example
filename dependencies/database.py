from typing import Annotated

from fastapi import Depends

from database.db_alumnos import DBAlumnos
from database.db_grupos import DBGrupos
from database.db_integrantes import DBIntegrantes

__database_alumnos_instance = None
__database_grupos_instance = None
__database_integrantes_instance = None


def init_db():
    global __database_alumnos_instance
    global __database_grupos_instance
    global __database_integrantes_instance
    __database_alumnos_instance = DBAlumnos()
    __database_grupos_instance = DBGrupos()
    __database_integrantes_instance = DBIntegrantes()


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


def get_db_integrantes() -> DBIntegrantes:
    global __database_integrantes_instance
    if __database_integrantes_instance is None:
        raise RuntimeError("Database instance not initialized.")
    return __database_integrantes_instance


DBAlumnosDep = Annotated[DBAlumnos, Depends(get_db_alumnos)]
DBGruposDep = Annotated[DBGrupos, Depends(get_db_grupos)]
DBIntegrantesDep = Annotated[DBIntegrantes, Depends(get_db_integrantes)]
