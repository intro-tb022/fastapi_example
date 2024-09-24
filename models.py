from pydantic import BaseModel

class Alumno(BaseModel):
    padron: int
    nombre: str
    apellido: str
    edad: int | None = None

class AlumnoCreate(BaseModel):
    nombre: str
    apellido: str
    edad: int | None = None


class Error(BaseModel):
    detail: str


alumnos: list[Alumno] = [
    Alumno(padron=94557, nombre="Federico", apellido="Esteban"),
    Alumno(padron=95557, nombre="Daniela", apellido="Riesgo"),
    Alumno(padron=98713, nombre="Juan Ignacio", apellido="Kristal")
]
