from models.alumno import AlumnoBase
from models.grupo import GrupoBase
from models.integrante import IntegranteBase


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


class IntegrantePublicWithRelations(IntegrantePublic):
    alumno: AlumnoPublic
    grupo: GrupoPublic


class GrupoPublicWithIntegrantes(GrupoPublic):
    integrantes: list[IntegrantePublicWithAlumno] = []
