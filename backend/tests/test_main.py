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


def test_read_main():
    response = client.get("/")
    assert response.status_code == 404
