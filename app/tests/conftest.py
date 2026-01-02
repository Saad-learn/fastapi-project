import pytest
from fastapi.testclient import TestClient
from app.main import app

def client():
    return TestClient(app)

def admin_token():
    from app.auth.authentication import create_access_token
    return create_access_token(user_id=1)

def org_id():
    return 1

def user_id():
    return 1
