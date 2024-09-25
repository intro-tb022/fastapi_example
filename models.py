from typing import List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship

class GrupoBase(SQLModel):
   nombre: str

class Grupo(GrupoBase, table=True):
   id: int = Field(primary_key=True)

   alumnos: list["Alumno"] = Relationship(back_populates="grupo")

class GrupoPublic(GrupoBase):
    id: int
    alumnos: list["Alumno"] = []

class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    grupo_id: int | None = Field(default=None, foreign_key="grupo.id")
    grupo: Grupo | None = Relationship(back_populates="alumnos")

class AlumnoPublic(AlumnoBase):
    padron: int
    grupo: Grupo | None = None

class Error(BaseModel):
    detail: str
