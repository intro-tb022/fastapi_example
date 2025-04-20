from sqlmodel import Field, Relationship, SQLModel

from src.models.grupo import Grupo
from src.models.integrante import Integrante


class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)


class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    grupos: list[Grupo] | None = Relationship(link_model=Integrante)


class AlumnoUpsert(AlumnoBase):
    pass
