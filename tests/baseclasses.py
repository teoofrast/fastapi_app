class BaseCheckPost:
    """
    Класс для проверки POST-запросов
    """

    def __init__(self, response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_json = response.json()

    def assert_response(self, status_code: int):
        assert self.response.status_code == status_code, f'Был возвращен статус-код: {self.response_status_code}, а ожидался: {status_code}'
        return self

    def assert_response_json_first(self, answer: dict[str, str]):
        assert self.response_json == answer, f'Был возвращен ответ {self.response_json}, а ожидался: {answer}'
        return self

    def assert_response_json_second(self, answer):
        assert self.response_json[
                   'message'] == answer, f"Был возвращен ответ {self.response_json['message']}, а ожидался: {answer}"
        return self
