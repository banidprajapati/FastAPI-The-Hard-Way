from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator


from backend.core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:  # new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
