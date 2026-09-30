import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from src.main import app

from unittest.mock import patch


client = TestClient(app)


def test_lab2_health():
    mock_time_value = datetime(2026, 9, 29, 16, 0 , 0)
    with patch("src.main.datetime") as mock_datetime:
        mock_datetime.now.return_value = mock_time_value


        response = client.get("/health")
        assert response.status_code == 200
        assert datetime.fromisoformat(response.json()["time"])
        assert response.json() == {"time": f"{mock_time_value.isoformat()}"}


def test_root_returns_not_found():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


@pytest.mark.parametrize(
    "name, expected",
    [
        ("World", "Hello World"),
        ("james", "Hello james"),
        ("BoB", "Hello BoB"),
        ("100", "Hello 100"),
    ],
)
def test_hello_returns_greeting(name, expected):
    response = client.get(f"/hello?name={name}")
    assert response.status_code == 200
    assert response.json() == {"message": expected}


def test_hello_requires_name_parameter():
    response = client.get("/hello")
    assert response.status_code == 422
    body = response.json()
    assert body["detail"][0]["loc"] == ["query", "name"]
    assert body["detail"][0]["type"] == "missing"


def test_hello_ignores_extra_parameters():
    response = client.get("/hello?name=james&extra=ignored")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello james"}


def test_docs_endpoint_serves_swagger_ui():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_openapi_json_is_v3():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["openapi"].startswith("3.")
