import json
import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_url_success(client):
    response = client.post(
        "/analyze-url",
        json={"url": "https://example.com?user=admin"}
    )

    data = response.get_json()
    assert response.status_code == 200
    assert data["Domain"]["value"] == "example.com"


def test_analyze_url_invalid(client):
    response = client.post(
        "/analyze-url",
        json={"url": "invalid-url"}
    )

    data = response.get_json()
    assert "error" in data


def test_analyze_url_missing_payload(client):
    response = client.post("/analyze-url", json={})
    assert response.status_code == 400
