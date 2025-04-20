from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from sqlmodel import Session

from database.db_grupos import DBGrupos
from dependencies.database import get_db_grupos
from dependencies.sqlmodel import get_session
from main import app
from models.alumno import Alumno
from models.grupo import Grupo
from models.integrante import Integrante

client = TestClient(app)

mock_session = MagicMock(Session)
app.dependency_overrides[get_session] = lambda: mock_session

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


def test_inscribir():
    grupo_id = 1
    padron = 12345
    nombre = "Grupo Test"

    integrantes = [
        Integrante(
            alumno=Alumno(padron=padron, nombre="Pepito", apellido="Test"), grupo=Grupo(id=grupo_id, nombre=nombre)
        )
    ]
    mock_db.inscribir.return_value = Grupo(id=grupo_id, nombre=nombre, integrantes=integrantes)

    data = {"padron": padron}
    response = client.post(f"/grupos/{grupo_id}/integrantes", json=data)

    assert response.status_code == 201
    content = response.json()
    assert content["id"] == grupo_id
    assert content["nombre"] == nombre
    assert content["integrantes"] == [
        {"nota": None, "alumno": {"nombre": "Pepito", "apellido": "Test", "edad": None, "padron": padron}}
    ]


def test_desinscribir():
    grupo_id = 1
    padron = 12345
    nombre = "Grupo Test"

    mock_db.desinscribir.return_value = Grupo(id=grupo_id, nombre=nombre, integrantes=[])

    response = client.delete(f"/grupos/{grupo_id}/integrantes/{padron}")

    assert response.status_code == 200
    content = response.json()
    assert content["id"] == grupo_id
    assert content["nombre"] == nombre
    assert content["integrantes"] == []
