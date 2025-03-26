from sqlmodel import Field, Relationship, SQLModel

from src.models.integrante import Integrante


class GrupoBase(SQLModel):
    nombre: str


class Grupo(GrupoBase, table=True):
    id: int = Field(primary_key=True)

    integrantes: list[Integrante] | None = Relationship()

    # alumnos: list["Alumno"] | None = Relationship(
    #     back_populates="grupos", link_model=Integrante
    # )


class GrupoUpsert(GrupoBase):
    pass
