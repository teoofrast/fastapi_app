import pytest
import os

from dotenv import load_dotenv

from src.models import *
from src.database import engine

load_dotenv()


@pytest.fixture(scope='session')
def prepare_database():
    assert os.getenv("MOD") == "TEST"
