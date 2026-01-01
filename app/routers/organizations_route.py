from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.organization_schema import OrganizationCreate, OrganizationOut
from app.models.organization_mdl import Organization
from app.auth.dependencies import get_db, get_current_user
from app.auth.permissions import admin_only

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("/", response_model=OrganizationOut)
def create_org(data: OrganizationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    admin_only(user)
    existing = db.query(Organization).filter(Organization.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Organization already exists")
    org = Organization(name=data.name, owner_id=user.id)
    db.add(org)
    db.commit()
    db.refresh(org)
    return org

