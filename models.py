from typing import List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel

class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class Alumno(AlumnoBase, table=True):
   padron: int = Field(primary_key=True)

class AlumnoCreate(AlumnoBase):
    pass

class Error(BaseModel):
    detail: str
