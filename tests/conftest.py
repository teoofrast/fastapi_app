import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, select

from src.database import engine
from src.models import Document

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

