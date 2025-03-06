from pydantic import BaseModel, Field
from sqlmodel import SQLModel

class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class Alumno(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class AlumnoUpsert(AlumnoBase):
    pass

class Error(BaseModel):
    detail: str
