from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    viewer = "viewer"

class OrganizationCreate(BaseModel):
    name : str

class OrganizationOut(BaseModel):
    id : int
    name : str

    class Config:
        from_attributes = True

class RoleUpdate(BaseModel):
    role : RoleEnum