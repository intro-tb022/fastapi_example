from models.alumno import AlumnoBase
from models.grupo import GrupoBase

class AlumnoPublic(AlumnoBase):
    padron: int

class GrupoPublic(GrupoBase):
    id: int

class AlumnoPublicWithGroup(AlumnoPublic):
    grupo: GrupoPublic | None = None

class GrupoPublicWithAlumnos(GrupoPublic):
    id: int
    alumnos: list[AlumnoPublic] = []
