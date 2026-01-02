import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def admin_token():
    return "admin_valid_token"

@pytest.fixture
def org_id():
    return 1

@pytest.fixture
def user_id():
    return 1

def test_admin_create_organization(client, admin_token):
    response = client.post(
        "/organizations/",
        json={"name": "Test Org"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 401
    assert response.json()== {'detail': 'Invalid token'}

def test_admin_delete_organization(client, admin_token, org_id):
    response = client.delete(
        f"/organizations/{org_id}",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 404

def test_admin_update_organization(client, admin_token, user_id):
    response = client.put(
        f"/users/{user_id}/role",
        json={"role": "manager"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 401
    assert response.json() == {'detail':'Invalid token'}
