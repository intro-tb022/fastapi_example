from fastapi import HTTPException
import pytest
from sqlmodel import SQLModel, Session, StaticPool, create_engine

from src.models.grupo import GrupoUpsert
from src.database.db_grupos import DBGrupos


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def db():
    return DBGrupos()


grupo_a_crear = GrupoUpsert(nombre="Grupo Test")


class TestDBGrupos:
    def test_add(self, db: DBGrupos, session: Session):
        grupo = db.add(session, grupo_a_crear)

        assert grupo.id == 1
        assert db.list(session) == [grupo]

    def test_list_vacio(self, db: DBGrupos, session: Session):
        assert db.list(session) == []

    def test_list_no_vacio(self, db: DBGrupos, session: Session):
        grupo1 = db.add(session, grupo_a_crear)
        grupo2 = db.add(session, grupo_a_crear)

        assert db.list(session) == [grupo1, grupo2]

    def test_find_valido(self, db: DBGrupos, session: Session):
        grupo = db.add(session, grupo_a_crear)

        assert db.find(session, 1) == grupo

    def test_find_no_existente(self, db: DBGrupos, session: Session):
        try:
            db.find(session, 3)
            assert False
        except HTTPException as e:
            assert str(e) == "404: Grupo not found"
