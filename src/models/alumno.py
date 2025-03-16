from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

class AlumnoUpsert(AlumnoBase):
    pass

class Error(BaseModel):
    detail: str
