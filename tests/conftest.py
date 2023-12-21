import pytest

from src.config import settings
from src.database import Base, sync_engine


@pytest.fixture(scope='session', autouse=True)
def setup_bd():
    print(f'{settings.DB_NAME=}')
    assert settings.MODE == 'TEST'
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

