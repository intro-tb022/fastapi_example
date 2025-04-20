from fastapi import APIRouter

from src.dependencies.database import DBIntegrantesDep
from src.dependencies.sqlmodel import SessionDep
from src.models.public import IntegrantePublicWithRelations

router = APIRouter()


@router.put("/{grupo_id}/{padron}")
def cargar_nota(
    session: SessionDep, db: DBIntegrantesDep, grupo_id: int, padron: int, nota: int
) -> IntegrantePublicWithRelations:
    integrante = db.poner_nota(session, grupo_id, padron, nota)
    return integrante
