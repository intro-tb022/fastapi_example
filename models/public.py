from models.alumno import AlumnoBase
from models.grupo import GrupoBase
from models.materia import MateriaBase

class AlumnoPublic(AlumnoBase):
    padron: int

class GrupoPublic(GrupoBase):
    id: int

class AlumnoPublicWithRelations(AlumnoPublic):
    grupo: GrupoPublic | None = None
    materias: list["MateriaPublic"] = []

class GrupoPublicWithAlumnos(GrupoPublic):
    id: int
    alumnos: list[AlumnoPublic] = []

class MateriaPublic(MateriaBase):
    id: int

class MateriaPublicWithAlumnos(MateriaPublic):
    alumnos: list[AlumnoPublic] = []
