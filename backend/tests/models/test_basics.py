from db import db
from models import BasicsModel

from .base import TestModelBase


class TestBasics(TestModelBase):
    def test_jsonifying(self):
        expected_json = {
            "name": "He",
            "summary": "Knows nothing, you know",
            "email": "un@kn.own",
        }
        basics = BasicsModel(*list(expected_json.values()))
        assert basics.json() == expected_json

    def test_adding_basics(self):
        expected_json = {
            "name": "He",
            "summary": "Knows nothing, you know",
            "email": "un@kn.own",
        }
        basics = BasicsModel(*list(expected_json.values()))
        basics.save_to_db()
        assert basics in db.session
        fetched = basics.fetch()
        assert fetched.json() == expected_json

    def test_modifying_basics(self):
        old_json = {
            "name": "He",
            "summary": "Knows nothing, you know",
            "email": "un@kn.own",
        }
        expected_json = {
            "name": "She",
            "summary": "Knows something",
            "email": "why@do.you",
        }
        basics = BasicsModel(*list(old_json.values()))
        basics.save_to_db()
        assert basics in db.session

        new_basics = BasicsModel(*list(expected_json.values()))
        new_basics.save_to_db()
        assert new_basics in db.session
        assert basics not in db.session
        assert new_basics.json() == expected_json
