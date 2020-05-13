import pytest

from db import db
from models import BasicsModel

from .base import TestModelBase


@pytest.mark.model
class TestBasics(TestModelBase):
    expected_json = {
        "name": "He",
        "summary": "Knows nothing, you know",
        "email": "un@kn.own",
    }

    def test_jsonifying(self):
        basics = BasicsModel(**self.expected_json)
        assert basics.json() == self.expected_json

    def test_fetching(self):
        basics = BasicsModel(**self.expected_json)
        basics.save_to_db()
        fetched = basics.fetch()
        assert isinstance(fetched, BasicsModel)
        assert hasattr(fetched, "email")
        assert fetched.name == basics.name

    def test_adding_basics(self):
        basics = BasicsModel(**self.expected_json)
        basics.save_to_db()
        assert basics in db.session
        fetched = basics.fetch()
        assert fetched.json() == self.expected_json

    def test_modifying_basics(self):
        new_json = {
            "name": "She",
            "summary": "Knows something",
            "email": "why@do.you",
        }
        basics = BasicsModel(**self.expected_json)
        basics.save_to_db()
        assert basics in db.session

        new_basics = BasicsModel(**new_json)
        new_basics.save_to_db()
        assert new_basics in db.session
        assert basics not in db.session
        assert new_basics.json() == new_json
