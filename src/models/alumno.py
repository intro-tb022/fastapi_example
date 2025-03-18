from pydantic import BaseModel
from sqlmodel import Relationship, SQLModel, Field

from src.models.grupo import Grupo


class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)


class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    grupo_id: int | None = Field(default=None, foreign_key="grupo.id")
    grupo: Grupo | None = Relationship(back_populates="alumnos")


class AlumnoUpsert(AlumnoBase):
    pass


class Error(BaseModel):
    detail: str
