from fastapi.testclient import TestClient
from app.main import app


def test_items_flow():
    client = TestClient(app)
    assert client.get("/items/").status_code == 200
    response = client.post("/items/", json={"id": 2, "name": "gadget", "score": 7})
    assert response.status_code == 200
    assert (
        client.post("/items/", json={"id": 2, "name": "dup", "score": 1}).status_code
        == 409
    )
