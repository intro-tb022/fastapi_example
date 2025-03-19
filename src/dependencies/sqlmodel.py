import os
from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import Session, create_engine

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
SQLITE_FILE_PATH = os.path.join(root, "database.db")


def init_engine():
    return create_engine(f"sqlite:///{SQLITE_FILE_PATH}", echo=True)
