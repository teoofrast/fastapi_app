from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from pydantic import BaseModel, EmailStr, field_validator




Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)


class UserDAL(object):
    """Слой для взаимодействия с моделью пользователя."""
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self, name: str, surname: str, email: str,
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user



app = FastAPI(title='My API')

user_router = APIRouter()




main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/users', tags=['users'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)