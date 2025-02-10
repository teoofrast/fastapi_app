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











app = FastAPI(title='My API')

user_router = APIRouter()




main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/users', tags=['users'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)