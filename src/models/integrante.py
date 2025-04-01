from sqlmodel import Field, Relationship, SQLModel

MAX_SIZE: int = 4


class IntegranteBase(SQLModel):
    nota: int | None = Field(default=None, ge=1, le=10)


class Integrante(IntegranteBase, table=True):

    grupo_id: int | None = Field(
        nullable=False, foreign_key="grupo.id", primary_key=True
    )
    grupo: "Grupo" = Relationship()

    alumno_padron: int | None = Field(
        nullable=False, foreign_key="alumno.padron", primary_key=True
    )
    alumno: "Alumno" = Relationship()
