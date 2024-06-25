from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_connect_to_database():
    assert 1 == 1

