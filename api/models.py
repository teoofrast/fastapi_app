import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


LETTER_MATCH_PATTERN = re.compile(r'^[а-яА-Яa-zA-Z\-]+$')


class TunedModel(BaseModel):
    class Config:
        """Преобразование не dict объекты в JSON формат"""
        orm_mode = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail='Имя должно состоять только из букв'
            )
        return value

    @field_validator('surname')
    @classmethod
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail='Фамилия должна состоять только из букв'
            )
        return value
