from fastapi.testclient import TestClient

from main import app, get_db
from tests.fixtures.test_db import override_get_db


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
