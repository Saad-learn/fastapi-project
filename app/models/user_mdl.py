from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.database.db import Base
import enum
from app.models.organization_mdl import Organization

class Role(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    viewer = "viewer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Role))
    organization_id = Column(Integer, ForeignKey("organizations.id"))
