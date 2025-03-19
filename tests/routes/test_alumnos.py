from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from src.models.grupo import Grupo
from src.database.db_grupos import DBGrupos
from src.main import app
from src.models.alumno import Alumno
from src.database.db_alumnos import DBAlumnos
from src.dependencies.database import get_db_alumnos, get_db_grupos

client = TestClient(app)

mock_db = MagicMock(DBAlumnos)
app.dependency_overrides[get_db_alumnos] = lambda: mock_db
mock_db_grupos = MagicMock(DBGrupos)
app.dependency_overrides[get_db_grupos] = lambda: mock_db_grupos


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


def test_get_alumno():
    mock_db.find.return_value = Alumno(
        padron=1, nombre="Juan", apellido="Perez", edad=20
    )

    response = client.get(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["padron"] == 1
    assert content["nombre"] == "Juan"
    assert content["apellido"] == "Perez"
    assert content["edad"] == 20


def test_create_alumno():
    mock_db.add.return_value = Alumno(
        padron=1, nombre="Test", apellido="Apellido", edad=19
    )

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.post("/alumnos/", json=data)

    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1


def test_update_alumno():
    mock_db.update.return_value = Alumno(
        padron=1, nombre="Test", apellido="Apellido", edad=19
    )

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.put("/alumnos/1", json=data)

    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1


def test_delete_alumno():
    mock_db.delete.return_value = Alumno(
        padron=1, nombre="Test", apellido="Apellido", edad=19
    )

    response = client.delete(
        "/alumnos/1",
    )

    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1


def test_asignar_grupo():
    grupo_id = 1
    grupo = Grupo(id=grupo_id, nombre="Grupo Test")
    mock_db_grupos.find.return_value = grupo
    padron = 1
    mock_db.inscribirse_a_grupo.return_value = Alumno(
        padron=padron, nombre="Test", apellido="Apellido", edad=19, grupo=grupo
    )

    response = client.put(
        f"/alumnos/{padron}/asignar_grupo",
        params={"grupo_id": grupo_id},
    )

    assert response.status_code == 200
    content = response.json()
    assert content["grupo"] != None
    assert content["grupo"]["id"] == grupo_id
