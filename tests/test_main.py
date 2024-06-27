from baseclasses import BaseCheck


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
    r = BaseCheck(response)
    r.assert_response(200).assert_response_json({"message": 'Image uploaded'})
