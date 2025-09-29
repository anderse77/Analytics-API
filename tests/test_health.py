from fastpi.testclient import TestClient
from app.main import app


def test_live():
    client = TestClient(app)
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
