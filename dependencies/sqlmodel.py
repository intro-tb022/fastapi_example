import os
from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session, create_engine

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SQLITE_FILE_PATH = os.path.join(root, "database.db")


engine = None


def init_engine():
    global engine
    engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}", echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
