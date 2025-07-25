from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)  # new
    return app


app = start_application()
