from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    viewer = "viewer"

class UserCreate(BaseModel):
    email : EmailStr
    password : str
    role : RoleEnum

class UserOut(BaseModel):
    id : int 
    email : EmailStr
    role : RoleEnum

    class Config:
        from_attributes = True

class RoleUpdate(BaseModel):
    role : RoleEnum