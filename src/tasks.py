from celery import Celery
import pytesseract
from PIL import Image
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError

from src.database import engine
from sqlalchemy.orm import sessionmaker
from src.models import DocumentsText


Session = sessionmaker(bind=engine)
session = Session()


# Создаем экземпляр Celery
celery = Celery(
                'tasks',
                result_backend='rpc://teoofrast:teoofrast@localhost:5672/',
                broker='amqp://teoofrast:teoofrast@localhost:5672/'
                )
celery.conf.broker_connection_retry_on_startup = True


@celery.task(name='src.tasks.extract_text_from_image')
def extract_text_from_image(file_path, image_id):
    # Используем pytesseract для извлечения текста из изображения
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img, lang="rus")
    try:
        text_p = DocumentsText(id_doc=image_id, text=text)
        session.add(text_p)
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=500, detail="Failed to save text to database")
    finally:
        session.close()
    return text
