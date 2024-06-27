import os
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, select

from src.database import engine
from src.models import Document


from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

Session = sessionmaker(bind=engine)
session = Session()


@pytest.fixture()
def connection_to_postgres_db():
    """
    Проверяет соединение с БД и создает один документ
    """
    d = Document(path='shared_data/7750b6b9-5c99-49f1-98ff-f0c0e5903b09_dsa2.jpeg')
    session.add(d)
    session.commit()
    session.close()

    query = session.query(Document)
    yield query
    session.query(Document).delete()
    session.commit()
    session.close()


@pytest.fixture()
def image_prebuild():
    file_content = b"Test image content"
    file_name = "123.jpg"
    files = {'file': (file_name, file_content, 'image/jpg')}
    response = client.post("/upload_doc", files=files)
    yield response
    file_path = response.json()['path']
    os.remove(file_path)
