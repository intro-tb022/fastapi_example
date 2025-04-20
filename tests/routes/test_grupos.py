from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from database.db_grupos import DBGrupos
from dependencies.database import get_db_grupos
from main import app
from models.alumno import Alumno
from models.grupo import Grupo, GrupoUpsert
from models.integrante import Integrante, IntegranteCreate
from tests.mock_utils import mock_session

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

    mock_db.list.assert_called_once_with(mock_session)


def test_get_grupo():
    id = 1
    mock_db.find.return_value = Grupo(id=id, nombre="Grupo 1")

    response = client.get(
        f"/grupos/{id}",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["id"] == id
    assert content["nombre"] == "Grupo 1"

    mock_db.find.assert_called_once_with(mock_session, id)


def test_create_grupo():
    id = 1
    mock_db.add.return_value = Grupo(id=id, nombre="Grupo Test")

    data = {"nombre": "Grupo Test"}
    response = client.post("/grupos/", json=data)

    assert response.status_code == 201
    content = response.json()
    assert content["id"] == id
    assert content["nombre"] == "Grupo Test"

    mock_db.add.assert_called_once_with(mock_session, GrupoUpsert(nombre="Grupo Test"))


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

    mock_db.inscribir.assert_called_once_with(mock_session, grupo_id, IntegranteCreate(padron=padron))


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

    mock_db.desinscribir.assert_called_once_with(mock_session, grupo_id, padron)
