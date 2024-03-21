from fastapi import FastAPI, UploadFile, File, HTTPException
import os


from src.database import engine
from src.models import Document, DocumentsText
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import uuid
from src.tasks import extract_text_from_image

app = FastAPI()
Session = sessionmaker(bind=engine)
session = Session()
load_dotenv()


FORMAT = os.getenv('format')


@app.post("/upload_doc")
def upload_file(file: UploadFile = File(...)):
    file_format = file.filename.split('.')[-1]
    if file_format in FORMAT:
        filename = str(uuid.uuid4()) + "_" + file.filename
        file_path = f"src/docs/{filename}"
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        d = Document(path=file_path)
        session.add(d)
        session.commit()
        session.close()
        return {"message": "Image uploaded"}
    else:
        raise HTTPException(status_code=404, detail="Unsupported file format")


@app.post("/doc_delete/{files_id}")
def delete_file(files_id: int):
    files = session.query(Document).filter(Document.id == files_id).first()
    if files is None:
        raise HTTPException(status_code=404, detail="Image not exists")
    else:
        session.delete(files)
        session.commit()
        session.close()
        os.remove(files.path)
        return {"message": "Image deleted"}


@app.post("/doc_analyze/{image_id}")
def extract_text(image_id: int):
    image = session.query(Document).filter(Document.id == image_id).first()
    if image is None:
        raise HTTPException(status_code=404, detail="Image not exists")
    else:
        image_path = image.path
        result = extract_text_from_image.delay(image_path, image_id)

    return {'message': "Text extraction task submitted", "task_id": result.id, "image_path": image_path}


@app.get("/get_text/{text_id}")
def get_text(text_id: int):
    text = session.query(DocumentsText).filter(DocumentsText.id_doc == text_id).first()
    if text is None:
        raise HTTPException(status_code=404, detail="Text not exists")
    else:
        return {"text": text.text}

