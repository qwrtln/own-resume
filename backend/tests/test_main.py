import unittest
from copy import deepcopy

import pytest

from tests.base import client
from tests.fixtures.test_resume import test_resume


@pytest.mark.integration
class TestMain(unittest.TestCase):
    def test_read_resume(self):
        response = client.get("/resume")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), test_resume)

    def test_post_resume(self):
        response = client.post("/resume", data=test_resume)
        assert response.status_code == 405
        assert response.json()["detail"] == "Method Not Allowed"

    def test_get_wrong_data(self):
        response = client.get("/resume")
        broken_resume = deepcopy(test_resume)
        broken_resume["basics"]["name"] = "Mścisław Cabacki"
        assert response.status_code == 200
        assert response.json()["work"] == broken_resume["work"]
        assert response.json()["basics"] != broken_resume["basics"]

    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 404
