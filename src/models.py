from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    date = Column(TIMESTAMP, default=datetime.utcnow)
    text = relationship("DocumentsText", cascade="all, delete", backref="document")


class DocumentsText(Base):
    __tablename__ = 'documents_text'

    id = Column(Integer, primary_key=True)
    id_doc = Column(Integer, ForeignKey('document.id'), nullable=False, unique=True)
    text = Column(String)
