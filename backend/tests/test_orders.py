from fastapi.testclient import TestClient
from jose import jwt
from backend.app import app

SECRET = "dev-secret"
ALGO = "HS256"

client = TestClient(app)

def auth_header(sub="user-1"):
    token = jwt.encode({"sub": sub}, SECRET, algorithm=ALGO)
    return {"Authorization": f"Bearer {token}"}

def test_health():
    assert client.get("/health").json() == {"ok": True}

def test_list_orders_unauth():
    assert client.get("/orders").status_code == 401
