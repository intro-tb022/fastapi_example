from unittest.mock import MagicMock

import pytest
from database.grupo import DBGrupos
from dependencies.dependencies import get_database_grupos
from fastapi.testclient import TestClient
from main import app
from models.alumno import Alumno
from models.grupo import Grupo

mock_db = MagicMock(DBGrupos)
app.dependency_overrides[get_database_grupos] = lambda: mock_db

juanp = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)
juanp_data = {"padron": 1, "nombre": "Juan", "apellido": "Perez", "edad": 20}
grupo1 = Grupo(id=1, nombre="Grupo1", nota=5)
grupo2 = Grupo(id=2, nombre="Grupo2", nota=6, integrantes=[juanp])


@pytest.fixture
def client():
    return TestClient(app)


def test_list(client):
    mock_db.list.return_value = [
        grupo1,
        grupo2,
    ]

    response = client.get(
        "/grupos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2


def test_show(client):
    mock_db.find.return_value = grupo2

    response = client.get(
        "/grupos/2",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["id"] == 2
    assert content["nombre"] == "Grupo2"
    assert content["nota"] == 6
    assert content["integrantes"] == [juanp_data]
