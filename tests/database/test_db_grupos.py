from fastapi import HTTPException
import pytest
from sqlmodel import SQLModel, StaticPool, create_engine

from src.models.grupo import GrupoUpsert
from src.database.db_grupos import DBGrupos


@pytest.fixture
def engine():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    return engine


@pytest.fixture
def db(engine):
    return DBGrupos(engine)


grupo_a_crear = GrupoUpsert(nombre="Grupo Test")


class TestDBGrupos:
    def test_add(self, db: DBGrupos):
        grupo = db.add(grupo_a_crear)

        assert grupo.id == 1
        assert db.list() == [grupo]

    def test_list_vacio(self, db: DBGrupos):
        assert db.list() == []

    def test_list_no_vacio(self, db: DBGrupos):
        grupo1 = db.add(grupo_a_crear)
        grupo2 = db.add(grupo_a_crear)

        assert db.list() == [grupo1, grupo2]

    def test_find_valido(self, db: DBGrupos):
        grupo = db.add(grupo_a_crear)

        assert db.find(1) == grupo

    def test_find_no_existente(self, db: DBGrupos):
        try:
            db.find(3)
            assert False
        except HTTPException as e:
            assert str(e) == "404: Grupo not found"
