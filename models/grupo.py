from sqlmodel import Field, SQLModel, Relationship

class GrupoBase(SQLModel):
   nombre: str

class Grupo(GrupoBase, table=True):
   id: int = Field(primary_key=True)

   alumnos: list["Alumno"] = Relationship(back_populates="grupo")
