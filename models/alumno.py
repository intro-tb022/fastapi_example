from sqlmodel import Field, SQLModel, Relationship

from models.cursada import Cursada
from models.grupo import Grupo
from models.materia import Materia

class AlumnoBase(SQLModel):
    nombre: str
    apellido: str
    edad: int | None = Field(default=None, ge=17)

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase, table=True):
    padron: int = Field(primary_key=True)

    grupo_id: int | None = Field(default=None, foreign_key="grupo.id")
    grupo: Grupo | None = Relationship(back_populates="alumnos")

    materias: list[Materia] | None = Relationship(back_populates="alumnos", link_model=Cursada)
