import pytest
import warnings

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_connect_to_database(connection_to_postgres_db):
    """
    Проверяет создана ли запись в БД
    """
    assert len(connection_to_postgres_db.all()) != 0, "Запись не была создана"
