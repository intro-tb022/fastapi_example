from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_alumnos() -> None:
    response = client.get(
        "/alumnos/",
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 3


def test_create_alumno() -> None:
    data = {"nombre": "Test", "apellido": "Alumno", "edad": 19}
    response = client.post(
        "/alumnos/",
        json=data
    )
    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Test"
    assert content["apellido"] == "Alumno"
    assert content["edad"] == 19
    assert "padron" in content


def test_get_alumnos_again() -> None:
    response = client.get(
        "/alumnos/",
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 4