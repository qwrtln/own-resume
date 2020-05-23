from copy import copy

from fastapi.testclient import TestClient

from main import app, get_db
from tests.fixtures.test_resume import test_resume
from tests.fixtures.test_db import override_get_db


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_read_resume():
    response = client.get("/resume")
    assert response.status_code == 200
    assert response.json() == test_resume


def test_post_resume():
    response = client.post("/resume", data=test_resume)
    assert response.status_code == 405
    assert response.json()["detail"] == "Method Not Allowed"


def test_get_wrong_data():
    response = client.get("/resume")
    broken_resume = copy(test_resume)
    broken_resume["basics"]["name"] = "Mścisław Cabacki"
    assert response.status_code == 200
    assert response.json()["work"] == broken_resume["work"]
    assert response.json()["basics"] != broken_resume["basics"]


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
