from fastapi import HTTPException
from app.models.user_mdl import Role

def admin_only(user):
    if user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admin only action")




