from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class TokenData(BaseModel):
    access_token: str
    token_type: str
    
class UserDetails(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    
class Data(BaseModel):
    id: int
    message: str

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    hashed_password: str

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]

class ViewUser(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    created_datetime: datetime
    updated_datetime: datetime

    class Config:
        orm_mode = True
