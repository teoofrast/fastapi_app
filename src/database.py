from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()
DB_PORT = os.getenv("DB_POSTGRES_PORT")
DB_NAME = os.getenv("DB_POSTGRES_NAME")
DB_USER = os.getenv("DB_POSTGRES_USER")
DB_PASS = os.getenv("DB_POSTGRES_PASS")
DB_HOST = os.getenv("DB_POSTGRES_HOST")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")