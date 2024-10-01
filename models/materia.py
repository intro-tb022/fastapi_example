from sqlmodel import Field, Relationship, SQLModel

from models.cursada import Cursada

class Materia(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str

    alumnos: list["Alumno"] | None = Relationship(
        back_populates="materias", link_model=Cursada)
