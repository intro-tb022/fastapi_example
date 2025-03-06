
import os
from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
SQLITE_FILE_PATH = os.path.join(root, "database.db")

__engine = None

def init_sqlmodel():
    global __engine
    print(SQLITE_FILE_PATH)
    __engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}", echo=True)
    SQLModel.metadata.create_all(__engine)

def get_session() -> Generator[Session, None, None]:
   with Session(__engine) as session:
       yield session
SessionDep = Annotated[Session, Depends(get_session)]