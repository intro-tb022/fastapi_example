from sqlmodel import Field, Relationship, SQLModel


class GrupoBase(SQLModel):
    nombre: str


class Grupo(GrupoBase, table=True):
    id: int = Field(primary_key=True)

    integrantes: list["Alumno"] = Relationship(back_populates="grupo")


class GrupoUpsert(GrupoBase):
    pass
