from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.models.integrante import Integrante
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
        return self.__get(grupo_id, session)

    def add(self, grupo_a_crear: GrupoUpsert) -> Grupo:
        session = self.session()
        grupo = Grupo(nombre=grupo_a_crear.nombre)
        session.add(grupo)
        integrantes = [
            Integrante(
                grupo=grupo,
                alumno_padron=integrante.alumno_padron,
                nota=integrante.nota,
            )
            for integrante in grupo_a_crear.integrantes
        ]
        session.add_all(integrantes)
        session.commit()
        session.refresh(grupo)
        return grupo

    def __get(self, grupo_id: int, session: Session) -> Grupo:
        grupo = session.exec(select(Grupo).where(Grupo.id == grupo_id)).first()
        if grupo:
            return grupo
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found"
        )
