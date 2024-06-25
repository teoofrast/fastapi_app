from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_connect_to_database(connection_to_postgres_db):
    assert len(connection_to_postgres_db.all()) == 1, "Количество записей не равна единице"
    assert connection_to_postgres_db.first().id == 1, "Айди пользователя не равна единице"
    assert connection_to_postgres_db.first().path == 'shared_volume/7750b6b9-5c99-49f1-98ff-f0c0e5903b09_dsa2.jpeg', 'Неверный путь'
    assert connection_to_postgres_db.first().date is not None, 'Поле дата не заполнена'
