from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from database.db_alumnos import DBAlumnos
from dependencies.database import get_db_alumnos
from main import app
from models.alumno import Alumno, AlumnoUpsert
from tests.mock_utils import mock_session

client = TestClient(app)

mock_db = MagicMock(DBAlumnos)
app.dependency_overrides[get_db_alumnos] = lambda: mock_db


def test_get_alumnos():
    mock_db.list.return_value = [
        Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20),
        Alumno(padron=2, nombre="Maria", apellido="Lopez", edad=22),
    ]

    response = client.get(
        "/alumnos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2

    mock_db.list.assert_called_once_with(mock_session)


def test_get_alumno():
    padron = 12345
    mock_db.find.return_value = Alumno(padron=padron, nombre="Juan", apellido="Perez", edad=20)

    response = client.get(
        f"/alumnos/{padron}",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == padron
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20

    mock_db.find.assert_called_once_with(mock_session, padron)


def test_create_alumno():
    padron = 12345
    mock_db.add.return_value = Alumno(padron=padron, nombre="Test", apellido="Apellido", edad=19)

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.post("/alumnos/", json=data)

    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == padron

    mock_db.add.assert_called_once_with(mock_session, AlumnoUpsert(nombre="Test", apellido="Apellido", edad=19))


def test_update_alumno():
    padron = 12345
    mock_db.update.return_value = Alumno(padron=padron, nombre="Test", apellido="Apellido", edad=19)

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.put(f"/alumnos/{padron}", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == padron

    mock_db.update.assert_called_once_with(
        mock_session, padron, AlumnoUpsert(nombre="Test", apellido="Apellido", edad=19)
    )


def test_delete_alumno():
    padron = 12345
    mock_db.delete.return_value = Alumno(padron=padron, nombre="Test", apellido="Apellido", edad=19)

    response = client.delete(
        f"/alumnos/{padron}",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == padron

    mock_db.delete.assert_called_once_with(mock_session, padron)
