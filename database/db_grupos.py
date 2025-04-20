from fastapi import HTTPException, status
from sqlmodel import Session, select

from models.grupo import Grupo, GrupoUpsert
from models.integrante import Integrante, IntegranteCreate


class DBGrupos:
    def list(self, session: Session) -> list[Grupo]:
        return session.exec(select(Grupo)).all()

    def find(self, session: Session, grupo_id: int) -> Grupo:
        return self.__get(session, grupo_id)

    def add(self, session: Session, grupo_a_crear: GrupoUpsert) -> Grupo:
        grupo = Grupo(nombre=grupo_a_crear.nombre)
        session.add(grupo)
        integrantes = [
            Integrante(
                grupo=grupo,
                alumno_padron=integrante.padron,
                nota=integrante.nota,
            )
            for integrante in grupo_a_crear.integrantes
        ]
        session.add_all(integrantes)
        session.commit()
        session.refresh(grupo)
        return grupo

    def inscribir(self, session: Session, grupo_id: int, integrante_nuevo: IntegranteCreate) -> Grupo:
        grupo = self.__get(session, grupo_id)
        integrante = Integrante(grupo_id=grupo_id, alumno_padron=integrante_nuevo.padron)
        session.add(integrante)
        session.commit()
        session.refresh(grupo)
        return grupo

    def desinscribir(self, session: Session, grupo_id: int, padron: int) -> Grupo:
        grupo = self.__get(session, grupo_id)
        integrante = session.exec(
            select(Integrante).where(Integrante.alumno_padron == padron, Integrante.grupo_id == grupo_id)
        ).first()
        session.delete(integrante)
        session.commit()
        session.refresh(grupo)
        return grupo

    def __get(self, session: Session, grupo_id: int) -> Grupo:
        grupo = session.exec(select(Grupo).where(Grupo.id == grupo_id)).first()
        if grupo:
            return grupo
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found")
