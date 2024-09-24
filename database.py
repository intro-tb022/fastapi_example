from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

SQLITE_FILE_PATH = "database.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]
