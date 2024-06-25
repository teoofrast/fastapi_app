import pytest

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_connect_to_database(connection_to_postgres_db):
    """
    Проверяет создана ли запись в БД
    """
    assert len(connection_to_postgres_db.all()) != 0, "Запись не была создана"
    assert connection_to_postgres_db.first().id >= 1, "ID пользователя равна 0"
    assert connection_to_postgres_db.first().path == 'shared_data/7750b6b9-5c99-49f1-98ff-f0c0e5903b09_dsa2.jpeg', 'Неверный путь'
    assert connection_to_postgres_db.first().date is not None, 'Поле дата не заполнена'
