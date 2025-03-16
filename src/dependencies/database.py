from typing import Annotated

from fastapi import Depends

from src.database.database import Database

__database_instance = None

def init_db(engine):
    global __database_instance
    __database_instance = Database(engine)

def get_database() -> Database:
    global __database_instance
    if __database_instance is None:
        raise RuntimeError("Database instance not initialized.")
    return __database_instance

DatabaseDep = Annotated[Database, Depends(get_database)]