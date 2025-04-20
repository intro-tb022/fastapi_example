from fastapi import HTTPException, status
from sqlmodel import Session, select

from models.integrante import Integrante


class DBIntegrantes:
    def poner_nota(self, session: Session, grupo_id: int, padron: int, nota: int) -> Integrante:
        integrante = session.exec(
            select(Integrante).where(Integrante.grupo_id == grupo_id).where(Integrante.alumno_padron == padron)
        ).first()

        if not integrante:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found")

        integrante.nota = nota
        session.add(integrante)
        session.commit()
        session.refresh(integrante)
        return integrante
