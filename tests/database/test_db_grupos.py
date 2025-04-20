import pytest
from fastapi import HTTPException
from sqlmodel import Session, SQLModel, StaticPool, create_engine

from src.database.db_grupos import DBGrupos
from src.models.grupo import GrupoUpsert


@pytest.fixture
def engine():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    with Session(engine) as session:
        yield session


@pytest.fixture
def db():
    return DBGrupos()


grupo_a_crear = GrupoUpsert(nombre="Grupo Test")


class TestDBGrupos:
    def test_add(self, session: Session, db: DBGrupos):
        grupo = db.add(session, grupo_a_crear)

        assert grupo.id == 1
        assert db.list(session) == [grupo]

    def test_list_vacio(self, session: Session, db: DBGrupos):
        assert db.list(session) == []

    def test_list_no_vacio(self, session: Session, db: DBGrupos):
        grupo1 = db.add(session, grupo_a_crear)
        grupo2 = db.add(session, grupo_a_crear)

        assert db.list(session) == [grupo1, grupo2]

    def test_find_valido(self, session: Session, db: DBGrupos):
        grupo = db.add(session, grupo_a_crear)

        assert db.find(session, 1) == grupo

    def test_find_no_existente(self, session: Session, db: DBGrupos):
        try:
            db.find(session, 3)
            assert False
        except HTTPException as e:
            assert str(e) == "404: Grupo not found"
