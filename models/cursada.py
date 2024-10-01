from sqlmodel import Field, SQLModel

class Cursada(SQLModel, table=True):
    año: int

    materia_id: int | None = Field(nullable=False, foreign_key="materia.id", primary_key=True)
    alumno_padron: int | None = Field(nullable=False, foreign_key="alumno.padron", primary_key=True)
