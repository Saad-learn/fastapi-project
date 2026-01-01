from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Generator
import app.auth.authentication as authentication
from app.database.db import get_db
from app.models.user_mdl import User
from app.auth.authentication import decode_token
from jwt import ExpiredSignatureError, InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = db.query(User).get(int(user_id))
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )

    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )