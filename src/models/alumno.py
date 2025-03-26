from sqlmodel import Relationship, SQLModel, Field

from src.models.integrante import Integrante
from src.models.grupo import Grupo


class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)


class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    # integrantes: list[Integrante] | None = Relationship()

    grupos: list[Grupo] | None = Relationship(link_model=Integrante)


class AlumnoUpsert(AlumnoBase):
    pass
