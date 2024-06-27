from baseclasses import BaseCheckPost


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
    r = BaseCheckPost(response)
    r.assert_response(200).assert_response_json_first({"message": 'Image uploaded'})


def test_get_text_from_image(document_prebuild):
    """
    Проверка на постановки задач в очередь
    """
    response = document_prebuild
    r = BaseCheckPost(response)
    r.assert_response(200).assert_response_json_second("Text extraction task submitted")
