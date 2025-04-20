from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from sqlmodel import Session

from database.db_integrantes import DBIntegrantes
from dependencies.database import get_db_integrantes
from dependencies.sqlmodel import get_session
from main import app
from models.alumno import Alumno
from models.grupo import Grupo
from models.integrante import Integrante

client = TestClient(app)

mock_session = MagicMock(Session)
app.dependency_overrides[get_session] = lambda: mock_session

mock_db = MagicMock(DBIntegrantes)
app.dependency_overrides[get_db_integrantes] = lambda: mock_db


def test_poner_nota_valido():
    padron = 11111
    grupo_id = 1
    nota = 10

    grupo = Grupo(id=grupo_id, nombre="Grupo Test")
    alumno = Alumno(padron=padron, nombre="Alumno", apellido="Test")
    mock_db.poner_nota.return_value = Integrante(
        grupo_id=grupo_id, grupo=grupo, alumno_padron=padron, alumno=alumno, nota=nota
    )

    response = client.put(
        f"/integrantes/{grupo_id}/{padron}/poner_nota",
        params={"nota": nota},
    )

    assert response.status_code == 200
    content = response.json()
    assert content["grupo"] is not None
    assert content["grupo"]["id"] == grupo_id
    assert content["alumno"] is not None
    assert content["alumno"]["padron"] == padron
    assert content["nota"] == 10
