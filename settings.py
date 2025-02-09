"""Файл с настройками и конфигами для приложения"""

from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    'REAL_DATABASE_URL',
    default='postgresql+asyncpg://postgres:postgres@localhost:5432/postgres',
)
