from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.database.db import Base
import enum

class Role(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    viewer = "viewer"

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, index = True)
    owner_id = Column(Integer, ForeignKey("users.id"))