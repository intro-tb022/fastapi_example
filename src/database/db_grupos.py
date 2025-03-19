from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.alumno import Alumno
from src.models.grupo import Grupo, GrupoUpsert


class DBGrupos:
    def list(self, session: Session) -> list[Grupo]:
        return session.exec(select(Grupo)).all()

    def find(self, session: Session, grupo_id: int) -> Grupo:
        grupo = session.exec(select(Grupo).where(Grupo.id == grupo_id)).first()
        if grupo:
            return grupo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found"
        )

    def add(self, session: Session, grupo_a_crear: GrupoUpsert) -> Grupo:
        grupo = Grupo(**grupo_a_crear.model_dump())
        session.add(grupo)
        session.commit()
        session.refresh(grupo)
        return grupo
