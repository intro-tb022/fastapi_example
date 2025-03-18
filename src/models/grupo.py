from sqlmodel import Field, Relationship, SQLModel


class Grupo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str

    alumnos: list["Alumno"] = Relationship(back_populates="grupo")
