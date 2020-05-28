import shutil
import unittest
import warnings

from fastapi.testclient import TestClient

from main import app, get_db
from tests.fixtures.test_db import override_get_db, get_testing_db, DB_FILE

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


class TestBase(unittest.TestCase):
    def setUp(self):
        self.db = get_testing_db()
        shutil.copy(DB_FILE, f"{DB_FILE}_")

    def tearDown(self):
        try:
            shutil.move(f"{DB_FILE}_", DB_FILE)
        except FileNotFoundError:
            warnings.warn(
                "Trying to restore nonexistent DB file. This should never happen!"
            )
            raise
