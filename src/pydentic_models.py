from pydantic import BaseModel
from datetime import date


class DocumentCheck(BaseModel):
    id: int
    path: str
    date: date


class DocumentTextCheck(BaseModel):
    id: int
    id_doc: int
    text: str
