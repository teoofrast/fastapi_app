import uuid
import os

from src.database import engine
from sqlalchemy import text


def test_connection_to_db():
    """
    Проверяет соединение с базой данных путем выполнения сырого SQL
    """
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1


def test_upload_doc(prepare_client):
    """
    Проверяет ручку upload_doc (метод post)
    """
    client = prepare_client
    file_content = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\xec\x76\x8f\x8d\x00\x00\x00\x0cIDATx\x9c\x63\x00\x00\x00\x02\x00\x01\x0c\x0e\x1e\x15\x00\x00\x00\x00IEND\xaeB`\x82"
    file_name = f"test_{uuid.uuid4()}.png"
    response = client.post("/upload_doc", files={"file": (file_name, file_content, "image/png")})

    assert response.status_code == 200
    assert response.json()['message'] == "Image uploaded"
    assert os.path.exists(f"images/{response.json()['filename']}")


def test_upload_doc_invalid_format(prepare_client):
    """
    Проверяет ручку upload_doc с неверным форматом файла (метод post)
    """
    client = prepare_client
    file_content = b"dummy content"
    file_name = f"test_{uuid.uuid4()}.txt"
    response = client.post("/upload_doc", files={"file": (file_name, file_content, "text/plain")})
    assert response.status_code == 404
    assert response.json()['detail'] == "Unsupported file format"


def test_delete_doc(prepare_client, prepare_image):
    client = prepare_client
    image = prepare_image
    files_id = image.id
    response = client.delete(f"/doc_delete/{files_id}")
    assert response.status_code == 200
    assert response.json()['message'] == "Image deleted"


def test_delete_doc_without_image(prepare_client, prepare_image):
    client = prepare_client
    files_id = 100
    response = client.delete(f"/doc_delete/{files_id}")
    assert response.status_code == 404
    assert response.json()['detail'] == "Image not exists"
