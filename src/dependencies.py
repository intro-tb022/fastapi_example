from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session, create_engine

from src.database.database import Database

SQLITE_FILE_PATH = "path/to/db"

__database_instance = None
__engine = None

def init_dep():
    global __database_instance
    __database_instance = Database()

    __engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")

def get_database() -> Database:
    global __database_instance
    if __database_instance is None:
        raise RuntimeError("Repository instance not initialized.")
    return __database_instance
DatabaseDep = Annotated[Database, Depends(get_database)]

def get_session() -> Generator[Session, None, None]:
   with Session(__engine) as session:
       yield session
SessionDep = Annotated[Session, Depends(get_session)]