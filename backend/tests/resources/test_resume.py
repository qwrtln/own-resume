import json
from copy import copy

import pytest

from tests.fixtures.test_resume import test_resume
from .base import TestResourceBase


@pytest.mark.resource
class TestResume(TestResourceBase):
    def test_get(self):
        rv = self.client.get("/resume")
        assert rv.status_code == 200
        assert test_resume == json.loads(rv.data)

    def test_get_wrong_data(self):
        rv = self.client.get("/resume")
        broken_resume = copy(test_resume)
        broken_resume["basics"]["name"] = "Mścisław Cabacki"
        assert rv.status_code == 200
        assert broken_resume != json.loads(rv.data)

    def test_method_not_allowed(self):
        rv = self.client.post("/resume", data={"spam": "eggs"})
        assert rv.status_code == 405
        assert b"The method is not allowed for the requested URL." in rv.data
