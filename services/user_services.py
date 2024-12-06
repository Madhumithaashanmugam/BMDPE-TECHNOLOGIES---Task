import re
from passlib.context import CryptContext
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Models.user.models import User
from Models.user.schema import CreateUser, UpdateUser
import uuid

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def validate_email(email: str):
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
        raise HTTPException(status_code=400, detail="Invalid email format.")

def create_user(user_data: CreateUser, session: Session):
    validate_email(user_data.email)

    hashed_password = bcrypt_context.hash(user_data.hashed_password)
    new_user = User(
        id=str(uuid.uuid4()),
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        hashed_password=hashed_password
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

def update_user_by_id(id: str, user_data: UpdateUser, session: Session):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    session.commit()
    session.refresh(user)
    return user

def delete_user_by_id(id: str, session: Session):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"detail": "User deleted successfully"}
