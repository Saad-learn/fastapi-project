import pytest
from fastapi.testclient import TestClient
from app.main import app

def client():
    def fake_verify_token(token: str):
        return{"sub": "admin", "role": "admin"}
    app.dependency_overrides[verify_token] = fake_verify_token
    return TestClient(app)

def admin_token():
    from app.auth.authentication import create_access_token
    return create_access_token(user_id=1)

def org_id():
    return 1

def user_id():
    return 1

# conftest.py
import warnings
import pydantic._internal._config as _cfg

def pytest_configure():
    warnings.filterwarnings("ignore", category=_cfg.PydanticDeprecatedSince20)
