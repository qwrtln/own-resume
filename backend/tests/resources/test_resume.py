import json
from copy import copy

from .base import client
from resources.resume import resume


def test_get(client):
    rv = client.get("/resume")
    assert rv.status_code == 200
    assert resume == json.loads(rv.data)


def test_get_wrong_data(client):
    rv = client.get("/resume")
    broken_resume = copy(resume)
    broken_resume["basics"]["name"] = "Mścisław Cabacki"
    assert rv.status_code == 200
    assert broken_resume != json.loads(rv.data)


def test_method_not_allowed(client):
    rv = client.post("/resume", data={"spam": "eggs"})
    assert rv.status_code == 405
    assert b"The method is not allowed for the requested URL." in rv.data
