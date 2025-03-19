from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from src.dependencies.database import get_db_grupos
from src.database.db_grupos import DBGrupos
from src.main import app
from src.models.grupo import Grupo

client = TestClient(app)

mock_db = MagicMock(DBGrupos)
app.dependency_overrides[get_db_grupos] = lambda: mock_db


def test_get_grupos():
    mock_db.list.return_value = [
        Grupo(id=1, nombre="Grupo 1"),
        Grupo(id=2, nombre="Grupo 2"),
    ]

    response = client.get(
        "/grupos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2


def test_get_grupo():
    mock_db.find.return_value = Grupo(id=1, nombre="Grupo 1")

    response = client.get(
        "/grupos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["id"] == 1
    assert content["nombre"] == "Grupo 1"


def test_create_grupo():
    mock_db.add.return_value = Grupo(id=1, nombre="Grupo Test")

    data = {"nombre": "Grupo Test"}
    response = client.post("/grupos/", json=data)

    assert response.status_code == 201
    content = response.json()
    assert content["id"] == 1
    assert content["nombre"] == "Grupo Test"
