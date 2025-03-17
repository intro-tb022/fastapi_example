from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from src.main import app
from src.models.alumno import Alumno
from src.database.database import Database
from src.dependencies.database import get_database

client = TestClient(app)

mock_db = MagicMock(Database)
app.dependency_overrides[get_database] = lambda: mock_db

def test_get_alumnos():
    mock_db.list.return_value = [
        Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20),
        Alumno(padron=2, nombre="Maria", apellido="Lopez", edad=22)
    ]

    response = client.get(
        "/alumnos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2

def test_get_alumno():
    mock_db.find.return_value = Alumno(padron=1, nombre="Juan", apellido="Perez", edad=20)

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
    mock_db.add.return_value = Alumno(padron=1, nombre="Test", apellido="Apellido", edad=19)

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.post(
        "/alumnos/",
        json=data
    )
    
    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1

def test_update_alumno():
    mock_db.update.return_value = Alumno(padron=1, nombre="Test", apellido="Apellido", edad=19)

    data = {"nombre": "Test", "apellido": "Apellido", "edad": 19}
    response = client.put(
        "/alumnos/1",
        json=data
    )
    
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1

def test_delete_alumno():
    mock_db.delete.return_value = Alumno(padron=1, nombre="Test", apellido="Apellido", edad=19)

    response = client.delete(
        "/alumnos/1",
    )
    
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Apellido"
    assert content["edad"] == 19
    assert content["padron"] == 1