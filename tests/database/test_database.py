import pytest

from database.database import Database
from models import Alumno, AlumnoUpsert

juan = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)
juan_upsert = AlumnoUpsert(nombre="Juan", apellido="Perez", edad=20)
manuelin = Alumno(padron=2, nombre="Manuelin", apellido="Equis", edad=21)
manuelin_upsert = AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=21)


@pytest.fixture
def db():
    return Database()


class TestDatabase:
    def test_list_vacio(self, db):
        assert db.list() == []

    def test_list_no_vacio(self, db):
        db.cargar_alumnos([juan])

        assert db.list() == [juan]

    def test_add(self, db):
        db.add(juan_upsert)

        assert db.list() == [juan]

    def test_add_autoincrementa_padron(self, db):
        db.add(juan_upsert)
        db.add(manuelin_upsert)
        db.add(AlumnoUpsert(nombre="Fake", apellido="Alumno", edad=50))

        assert [a.padron for a in db.list()] == [1, 2, 3]

    def test_find_valido(self, db):
        db.add(juan_upsert)
        db.add(manuelin_upsert)

        assert db.find(2) == manuelin

    def test_find_no_existente(self, db):
        db.add(juan)

        try:
            db.find(3)
            assert False
        except Exception as e:
            assert str(e) == "404: Alumno not found"

    def test_delete_valido(self, db):
        db.add(juan_upsert)
        db.add(manuelin_upsert)

        assert db.delete(2) == manuelin
        assert db.list() == [juan]

    def test_delete_no_existente(self, db):
        db.add(juan)

        try:
            db.delete(2)
            assert False
        except Exception as e:
            assert str(e) == "404: Alumno not found"

    def test_update_valido(self, db):
        db.add(juan_upsert)
        db.add(manuelin_upsert)

        assert db.update(2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22)) == Alumno(
            padron=2, nombre="Manuelin", apellido="Equis", edad=22
        )
        assert db.list() == [juan, Alumno(padron=2, nombre="Manuelin", apellido="Equis", edad=22)]

    def test_update_no_existente(self, db):
        db.add(juan)

        try:
            db.update(2, AlumnoUpsert(nombre="Manuelin", apellido="Equis", edad=22))
            assert False
        except Exception as e:
            assert str(e) == "404: Alumno not found"
