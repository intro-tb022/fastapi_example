from unittest.mock import MagicMock

import pytest
from database.alumno import DBAlumnos
from dependencies.dependencies import get_database_alumnos
from fastapi.testclient import TestClient
from main import app
from models.alumno import Alumno


@pytest.fixture
def client():
    return TestClient(app)


mock_db = MagicMock(DBAlumnos)
app.dependency_overrides[get_database_alumnos] = lambda: mock_db


juanp = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)
mariap = Alumno(padron=2, nombre="Maria", apellido="Lopez", edad=22)
juanp_data = {"nombre": "Juan", "apellido": "Perez", "edad": 20}


def test_list(client):
    mock_db.list.return_value = [
        juanp,
        mariap,
    ]

    response = client.get(
        "/alumnos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2


def test_show(client):
    mock_db.find.return_value = juanp

    response = client.get(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_create(client):
    mock_db.add.return_value = juanp

    response = client.post("/alumnos/", json=juanp_data)

    assert response.status_code == 201
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_update(client):
    mock_db.update.return_value = juanp

    response = client.put("/alumnos/1", json=juanp_data)

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_delete(client):
    mock_db.delete.return_value = juanp

    response = client.delete(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20
