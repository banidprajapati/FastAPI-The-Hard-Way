from sqlalchemy.orm import Session


def get_user(email: str, db: Session):
    from db.models.models_user import User  # local import to break circular dependency

    user = db.query(User).filter(User.email == email).first()
    return user
