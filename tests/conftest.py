from fastapi import HTTPException

import pytest
import os
import time
from sqlalchemy.orm import sessionmaker

from src.database import engine
from src.models import Document, DocumentsText

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
    query = session.query(Document)
    yield query
    session.delete(d)
    session.commit()
    session.close()


@pytest.fixture()
def image_prebuild():
    file_name = "123.jpeg"
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "rb") as image:
        file_bytes = image.read()
    files = {'file': (file_name, file_bytes, 'image/jpg')}
    response = client.post("/upload_doc", files=files)
    yield response


@pytest.fixture()
def document_prebuild():
    global image_id
    image_id = session.query(Document).first().id
    response = client.post(f"/doc_analyze/{image_id}")
    yield response


@pytest.fixture()
def get_text_by_id():
    time.sleep(10)
    response = client.get(f"/get_text/{image_id}")
    yield response


@pytest.fixture()
def delete_image():
    response = client.delete(f"/doc_delete/{image_id}")
    yield response
