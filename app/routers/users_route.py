from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserOut, RoleUpdate
from app.models.user_mdl import User, Role
from app.auth.dependencies import get_db, get_current_user
from app.auth.permissions import admin_only
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["Users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=UserOut)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    admin_only(current_user)
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    user = User(
        email=data.email,
        password=pwd_context.hash(data.password),
        role=data.role,
        organization_id=current_user.organization_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/", response_model=list[UserOut])
def list_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role not in [Role.admin, Role.manager]:
        raise HTTPException(status_code=403, detail="Not allowed")

    return db.query(User).filter(
        User.organization_id == current_user.organization_id
    ).all()

@router.put("/{user_id}/role")
def update_role(
    user_id: int,
    data: RoleUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    admin_only(current_user)
    target = db.get(User, user_id)
    if not target:
        raise HTTPException(status_code=404, detail="User not found")
    if target.id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot change own role")
    target.role = data.role
    db.commit()
    return {"detail": "Role updated"}
