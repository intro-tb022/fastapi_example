from src.models.alumno import AlumnoBase
from src.models.grupo import GrupoBase


class AlumnoPublic(AlumnoBase):
    padron: int


class GrupoPublic(GrupoBase):
    id: int


class AlumnoPublicWithRelations(AlumnoPublic):
    grupo: GrupoPublic | None = None


class GrupoPublicWithIntegrantes(GrupoPublic):
    integrantes: list[AlumnoPublic] = []
