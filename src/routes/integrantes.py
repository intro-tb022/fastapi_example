from fastapi import APIRouter
from src.models.public import IntegrantePublicWithRelations
from src.dependencies.database import DBIntegrantesDep


router = APIRouter()


@router.put("/{grupo_id}/{padron}")
def cargar_nota(
    db: DBIntegrantesDep, grupo_id: int, padron: int, nota: int
) -> IntegrantePublicWithRelations:
    integrante = db.poner_nota(grupo_id, padron, nota)
    return integrante
