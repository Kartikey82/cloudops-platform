
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "service": "CloudOps Platform",
        "status": "running",
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_readiness_endpoint():
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_info_endpoint():
    response = client.get("/info")

    assert response.status_code == 200

    data = response.json()
    assert data["service"] == "CloudOps Platform API"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data
