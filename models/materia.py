from sqlmodel import Field, Relationship, SQLModel

from models.cursada import Cursada

class MateriaBase(SQLModel):
    nombre: str

class MateriaCreate(MateriaBase):
    pass

class Materia(MateriaBase, table=True):
    id: int = Field(primary_key=True)

    alumnos: list["Alumno"] | None = Relationship(
        back_populates="materias", link_model=Cursada)
