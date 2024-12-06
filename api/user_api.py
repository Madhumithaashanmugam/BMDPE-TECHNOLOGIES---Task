from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from Models.user.schema import CreateUser, UpdateUser, ViewUser
from services import user_services
from config.db.session import get_db
from Models.user.models import User


user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.post("/", response_model=ViewUser)
def create_user(user_data: CreateUser, db: Session = Depends(get_db)):
    return user_services.create_user(user_data, db)

@user_router.get("/", response_model=list[ViewUser])
def read_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@user_router.get("/{id}", response_model=ViewUser)
def read_user_by_id(id: str, db: Session = Depends(get_db)):
    user = db.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.put("/{id}", response_model=ViewUser)
def update_user(id: str, user_data: UpdateUser, db: Session = Depends(get_db)):
    return user_services.update_user_by_id(id, user_data, db)

@user_router.delete("/{id}")
def delete_user(id: str, db: Session = Depends(get_db)):
    return user_services.delete_user_by_id(id, db)
