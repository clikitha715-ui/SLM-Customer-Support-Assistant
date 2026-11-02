
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_invalid_question():
    response = client.post(
        "/generate",
        json={"question": "A"}
    )
    assert response.status_code == 422


def test_missing_question():
    response = client.post("/generate", json={})
    assert response.status_code == 422
