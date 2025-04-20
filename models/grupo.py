from sqlmodel import Field, Relationship, SQLModel

from models.integrante import Integrante, IntegranteCreate


class GrupoBase(SQLModel):
    nombre: str


class Grupo(GrupoBase, table=True):
    id: int = Field(primary_key=True)

    integrantes: list[Integrante] | None = Relationship(back_populates="grupo")


class GrupoUpsert(GrupoBase):
    integrantes: list[IntegranteCreate] = []
