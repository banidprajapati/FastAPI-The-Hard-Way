from sqlalchemy.orm import Session
from db.repository.repository_user import create_new_user
from schemas.schemas_user import UserCreate


def create_random_user(db: Session):
    user = UserCreate(email="ping@fastapitutorial.com", password="Hello!")
    user = create_new_user(user=user, db=db)
    return user
