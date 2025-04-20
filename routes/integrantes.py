from fastapi import APIRouter

from dependencies.database import DBIntegrantesDep
from dependencies.sqlmodel import SessionDep
from models.public import IntegrantePublicWithRelations

router = APIRouter()


@router.put("/{grupo_id}/{padron}/poner_nota")
def poner_nota(
    session: SessionDep, db: DBIntegrantesDep, grupo_id: int, padron: int, nota: int
) -> IntegrantePublicWithRelations:
    integrante = db.poner_nota(session, grupo_id, padron, nota)
    return integrante
