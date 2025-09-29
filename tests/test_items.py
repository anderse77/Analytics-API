from fastapi.testclient import TestClient
from app.main import app

def test_items_flow():
    client = TestClient(app)

    # list should work
    respones = client.get("/items/")
    assert response.status_code == 200
    initial = len(response.json())

    # create returns 201 Created
    response = client.post("/items/", json={"id": 2, "name": "gadget", "score": 7})
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 2 and body["name"] == "gadget" and body["score"] == 7

    # duplicate id should 409
    assert client.post("/items/", json={"id": 2, "name": "dup", "score": 1}).status_code == 409

    # list again should be +1
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == initial + 1