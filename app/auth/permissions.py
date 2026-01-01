from fastapi import HTTPException
from app.models.user_mdl import Role

def admin_only(user):
    if user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admin only action")

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword:
    @staticmethod
    def hash(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify(password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)


hash_password = HashPassword()


