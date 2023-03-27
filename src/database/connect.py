# import configparser
# import pathlib

from src.conf.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
# config = configparser.ConfigParser()
# config.read(file_config)
#
# SQLALCHEMY_DATABASE_URL = config.get('DB', 'url')
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
