from sqlmodel import Field, Relationship, SQLModel

from src.models.integrante import Integrante


class GrupoBase(SQLModel):
    nombre: str


class Grupo(GrupoBase, table=True):
    id: int = Field(primary_key=True)

    integrantes: list[Integrante] | None = Relationship()


class GrupoUpsert(GrupoBase):
    integrantes: list[Integrante] | None
