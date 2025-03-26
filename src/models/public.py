from src.models.integrante import IntegranteBase
from src.models.alumno import AlumnoBase
from src.models.grupo import GrupoBase


class AlumnoPublic(AlumnoBase):
    padron: int


class GrupoPublic(GrupoBase):
    id: int


class IntegrantePublic(IntegranteBase):
    pass


class AlumnoPublicWithRelations(AlumnoPublic):
    grupos: list[GrupoPublic] = []


class IntegrantePublicWithAlumno(IntegrantePublic):
    alumno: AlumnoPublic


class GrupoPublicWithIntegrantes(GrupoPublic):
    integrantes: list[IntegrantePublicWithAlumno] = []
