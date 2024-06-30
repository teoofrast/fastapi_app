Проект на FastAPI с тестами. Основная функция загрузка картинок в место хранения и считывание с него текста (только на русском языке). Также имеется возможность удаления информации о картинке с базы данных и удаление самой картинки с папки.
Проект реализован в контейнерах Docker. Имеется очередь задач Celery.
Тесты запускаются при помощи команды "docker-compose -f docker-compose.yml -f docker-compose-test.yml run --rm tests"

Project on FastAPI with tests. The main function is to load pictures into storage place and read text from it (only in Russian). There is also a possibility to delete information about a picture from the database and delete the picture itself from the folder. The project is implemented in Docker containers. There is a queue of Celery tasks.
Tests are run using the "docker-compose -f docker-compose -f docker-compose.yml -f docker-compose-test.yml run --rm tests" command.
