import shutil
import unittest

from fastapi.testclient import TestClient

from main import app, get_db
from tests.fixtures.test_db import override_get_db, get_testing_db, DB_FILE

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


class TestCrudBase(unittest.TestCase):
    def setUp(self):
        self.db = get_testing_db()
        shutil.copy(DB_FILE, f"{DB_FILE}_")

    def tearDown(self):
        shutil.move(f"{DB_FILE}_", DB_FILE)
