from typing import Annotated

from fastapi import Depends
from src.repository.repository import Repository

repository_instance = None

def init_dep():
    global repository_instance
    repository_instance = Repository()

def get_repository() -> Repository:
    global repository_instance
    if repository_instance is None:
        raise RuntimeError("Repository instance not initialized.")
    return repository_instance

RepositoryDep = Annotated[Repository, Depends(get_repository)]