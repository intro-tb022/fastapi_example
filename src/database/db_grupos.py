from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.grupo import Grupo, GrupoUpsert


class DBGrupos:
    def __init__(self, engine):
        self.engine = engine

    def session(self):
        with Session(self.engine) as session:
            return session

    def list(self) -> list[Grupo]:
        session = self.session()
        return session.exec(select(Grupo)).all()

    def find(self, grupo_id: int) -> Grupo:
        session = self.session()
        grupo = session.exec(select(Grupo).where(Grupo.id == grupo_id)).first()
        if grupo:
            return grupo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found"
        )

    def add(self, grupo_a_crear: GrupoUpsert) -> Grupo:
        session = self.session()
        grupo = Grupo(**grupo_a_crear.model_dump())
        session.add(grupo)
        session.commit()
        session.refresh(grupo)
        return grupo
