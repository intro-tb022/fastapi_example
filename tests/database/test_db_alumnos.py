import pytest
from fastapi import HTTPException
from sqlmodel import Session

from database.db_alumnos import DBAlumnos
from models.alumno import Alumno, AlumnoUpsert


@pytest.fixture
def db():
    return DBAlumnos()


juan_upsert = AlumnoUpsert(nombre="Juan", apellido="Perez", edad=20)
manuelin_upsert = AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=21)


class TestDBAlumnos:
    def test_add(self, session: Session, db: DBAlumnos):
        juan = db.add(session, juan_upsert)

        assert juan.padron == 1
        assert db.list(session) == [juan]

    def test_add_autoincrementa_padron(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)
        db.add(session, manuelin_upsert)
        db.add(session, AlumnoUpsert(nombre="Fake", apellido="Alumno", edad=50))

        assert [a.padron for a in db.list(session)] == [1, 2, 3]

    def test_list_vacio(self, session: Session, db: DBAlumnos):
        assert db.list(session) == []

    def test_list_no_vacio(self, session: Session, db: DBAlumnos):
        al1 = Alumno(nombre="Nombre1", apellido="Apellido1", edad=100)
        al2 = Alumno(nombre="Nombre2", apellido="Apellido2", edad=99)
        al1 = db.add(session, al1)
        al2 = db.add(session, al2)

        resultado = db.list(session)

        assert len(resultado) == 2
        assert resultado == [al1, al2]

    def test_find_valido(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)
        manuelin = db.add(session, manuelin_upsert)

        assert db.find(session, 2) == manuelin

    def test_find_no_existente(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)

        with pytest.raises(HTTPException, match="404: Alumno not found"):
            db.find(session, 3)

    def test_delete_valido(self, session: Session, db: DBAlumnos):
        juan = db.add(session, juan_upsert)
        manuelin = db.add(session, manuelin_upsert)

        borrado = db.delete(session, 2)
        assert borrado == manuelin
        assert db.list(session) == [juan]

    def test_delete_no_existente(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)

        with pytest.raises(HTTPException, match="404: Alumno not found"):
            db.delete(session, 2)

    def test_update_valido(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)
        db.add(session, manuelin_upsert)

        manuelin_updated = db.update(session, 2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22))
        assert manuelin_updated == Alumno(padron=2, nombre="Manuelin", apellido="Equis", edad=22)

    def test_update_no_existente(self, session: Session, db: DBAlumnos):
        db.add(session, juan_upsert)

        with pytest.raises(HTTPException, match="404: Alumno not found"):
            db.update(session, 2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22))
