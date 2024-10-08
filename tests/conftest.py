import uuid
import os
import shutil
import pytest

from unittest.mock import MagicMock

os.environ['MOD'] = "TEST"
from src.database import engine
from src.models import *
from src.main import app, session
from src.tasks import extract_text_from_image

from fastapi.testclient import TestClient


@pytest.fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='function')
def prepare_client():
    with TestClient(app, base_url='http://test') as client:
        yield client


@pytest.fixture(scope='session', autouse=True)
def prepare_dir():
    folder_path = "images"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    yield

    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


@pytest.fixture(scope='session')
def prepare_image():
    file_name = f"test_{uuid.uuid4()}.png"
    file_path = f"images/{file_name}"
    with open(file_path, 'wb') as f:
        f.write(
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\xec\x76\x8f\x8d\x00\x00\x00\x0cIDATx\x9c\x63\x00\x00\x00\x02\x00\x01\x0c\x0e\x1e\x15\x00\x00\x00\x00IEND\xaeB`\x82")
    new_image = Document(path=file_path)
    session.add(new_image)
    session.commit()
    yield new_image
    session.close()


@pytest.fixture
def prepare_extract_text_from_image(mocker, prepare_image):
    file_path = "test_image.png"
    image_id = prepare_image.id
    mock_text = "Тестовый текст"

    mock_image = MagicMock()
    mocker.patch("PIL.Image.open", return_value=mock_image)

    mocker.patch("pytesseract.image_to_string", return_value=mock_text)

    extract_text_from_image(file_path, image_id)
    yield image_id
