from copy import deepcopy

import pytest

from tests.base import client, TestBase
from tests.fixtures.test_resume import test_resume


@pytest.mark.integration
class TestMain(TestBase):
    def test_read_resume(self):
        response = client.get("/resume")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), test_resume)

    def test_post_resume(self):
        response = client.post("/resume", data=test_resume)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json()["detail"], "Method Not Allowed")

    def test_get_wrong_data(self):
        response = client.get("/resume")
        broken_resume = deepcopy(test_resume)
        broken_resume["basics"]["name"] = "Mścisław Cabacki"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["work"], broken_resume["work"])
        self.assertNotEqual(response.json()["basics"], broken_resume["basics"])

    def test_read_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 404)
