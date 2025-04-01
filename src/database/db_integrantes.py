from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.integrante import Integrante


class DBIntegrantes:
    def __init__(self, engine):
        self.engine = engine

    def session(self):
        with Session(self.engine) as session:
            return session

    def poner_nota(self, grupo_id: int, padron: int, nota: int) -> Integrante:
        session = self.session()
        integrante = session.exec(
            select(Integrante)
            .where(Integrante.grupo_id == grupo_id)
            .where(Integrante.alumno_padron == padron)
        ).first()

        if not integrante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found"
            )

        integrante.nota = nota
        session.add(integrante)
        session.commit()
        session.refresh(integrante)
        return integrante
