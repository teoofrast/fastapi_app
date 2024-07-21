from baseclasses import BaseCheckPost


def test_connect_to_database(connection_to_postgres_db):
    """
    Проверка на создание записи в БД
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


def test_get_text(get_text_by_id):
    """
    Проверка на наличие текста из картинки в БД
    """
    response = get_text_by_id
    r = BaseCheckPost(response)
    r.assert_response(200)
    assert response.json()[
               'text'] == "Не понимаю встречи\nвыпускников. Вам же\nдали шанс не видеть\nдруг друга до конца\nжизни, что не так?\n\f"

def test_delete_image(delete_image):
    """
    Проверка на удаление картинки из БД и папки хранения
    """
    response = delete_image
    r = BaseCheckPost(response)
    r.assert_response(200).assert_response_json_first({"message": 'Image deleted'})
