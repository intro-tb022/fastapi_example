from unittest.mock import MagicMock

from sqlmodel import Session

from dependencies.sqlmodel import get_session
from main import app

mock_session = MagicMock(Session)
app.dependency_overrides[get_session] = lambda: mock_session
