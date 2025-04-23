from pydantic import BaseModel


class Alumno(BaseModel):
    padron: int
    nombre: str
    apellido: str
    edad: int
    email: str
    notas: list[int] = []


class AlumnoUpsert(BaseModel):
    nombre: str
    apellido: str
    edad: int


class Error(BaseModel):
    detail: str
