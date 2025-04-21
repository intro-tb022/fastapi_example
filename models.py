from pydantic import BaseModel

class Alumno(BaseModel):
    padron: int
    nombre: str
    apellido: str
    edad: int
    notas: list[int] = []

class AlumnoUpsert(BaseModel):
    nombre: str
    apellido: str
    edad: int

class Error(BaseModel):
    detail: str
