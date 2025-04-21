from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

from models.grupo import Grupo
from models.integrante import Integrante


class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)


class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    grupos: list[Grupo] | None = Relationship(link_model=Integrante)


class AlumnoUpsert(AlumnoBase):
    pass


class FiltrosAlumno(SQLModel):
    nombre: str | None = None
    apellido: str | None = None
    edad: int | None = None
    padron: int | None = None
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
