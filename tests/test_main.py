import pytest


def test_connect_to_database(connection_to_postgres_db):
    """
    Проверяет создана ли запись в БД
    """
    assert len(connection_to_postgres_db.all()) != 0, "Запись не была создана"


def test_add_image_to_db(image_prebuild):
    """
    Проверка на успешное добавление картинки
    """
    response = image_prebuild
    assert response.status_code == 200
    assert response.json()['message'] == "Image uploaded"
