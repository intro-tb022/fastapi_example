from fastapi import HTTPException
import pytest
from sqlmodel import SQLModel, Session, StaticPool, create_engine

from src.models.alumno import Alumno, AlumnoUpsert
from src.database.db_alumnos import DBAlumnos


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
    return DBAlumnos()


juan_upsert = AlumnoUpsert(nombre="Juan", apellido="Perez", edad=20)
manuelin_upsert = AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=21)


@pytest.mark.usefixtures("session")
class TestDBAlumnos:
    def test_add(self, db: DBAlumnos, session: Session):
        juan = db.add(session, juan_upsert)

        assert juan.padron == 1
        assert db.list(session) == [juan]

    def test_add_autoincrementa_padron(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)
        db.add(session, manuelin_upsert)
        db.add(session, AlumnoUpsert(nombre="Fake", apellido="Alumno", edad=50))

        assert [a.padron for a in db.list(session)] == [1, 2, 3]

    def test_list_vacio(self, db: DBAlumnos, session: Session):
        assert db.list(session) == []

    def test_list_no_vacio(self, db: DBAlumnos, session: Session):
        al1 = Alumno(nombre="Nombre1", apellido="Apellido1", edad=100)
        al2 = Alumno(nombre="Nombre2", apellido="Apellido2", edad=99)
        al1 = db.add(session, al1)
        al2 = db.add(session, al2)

        resultado = db.list(session)

        assert len(resultado) == 2
        assert resultado == [al1, al2]

    def test_find_valido(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)
        manuelin = db.add(session, manuelin_upsert)

        assert db.find(session, 2) == manuelin

    def test_find_no_existente(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)

        try:
            db.find(session, 3)
            assert False
        except HTTPException as e:
            assert str(e) == "404: Alumno not found"

    def test_delete_valido(self, db: DBAlumnos, session: Session):
        juan = db.add(session, juan_upsert)
        manuelin = db.add(session, manuelin_upsert)

        borrado = db.delete(session, 2)
        assert borrado == manuelin
        assert db.list(session) == [juan]

    def test_delete_no_existente(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)

        try:
            db.delete(session, 2)
            assert False
        except Exception as e:
            assert str(e) == "404: Alumno not found"

    def test_update_valido(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)
        db.add(session, manuelin_upsert)

        assert db.update(
            session, 2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22)
        ) == Alumno(padron=2, nombre="Manuelin", apellido="Equis", edad=22)

    def test_update_no_existente(self, db: DBAlumnos, session: Session):
        db.add(session, juan_upsert)

        try:
            db.update(
                session, 2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22)
            )
            assert False
        except Exception as e:
            assert str(e) == "404: Alumno not found"
