FROM python:3.11.8-bullseye

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-rus

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod 777 /fastapi_app/src/docs

#CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000