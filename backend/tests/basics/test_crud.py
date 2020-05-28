import pytest
from sqlalchemy.exc import InterfaceError

from basics.crud import get_basics, update_basics
from basics.model import BasicsModel
from basics.schema import Basics
from tests.base import TestBase
from tests.fixtures.test_resume import test_resume


class BasicsMixin:
    new_basics = {
        "name": "He",
        "summary": "Knows nothing, you know",
        "email": "un@kn.own",
    }


@pytest.mark.crud
class TestBasicsCrud(TestBase, BasicsMixin):
    def test_get(self):
        basics = get_basics(self.db)
        self.assertIsInstance(basics, BasicsModel)
        self.assertEqual(basics.name, test_resume["basics"]["name"])

    def test_modifying(self):
        _ = get_basics(self.db)
        new_basics = Basics(**self.new_basics)
        db_basics = update_basics(self.db, new_basics)
        self.assertEqual(db_basics.name, new_basics.name)
        self.assertEqual(db_basics.email, new_basics.email)
        self.assertEqual(db_basics.summary, new_basics.summary)

    def test_basics_email_wrong_type(self):
        basics = get_basics(self.db)

        class FakeEmail:
            pass

        basics.email = FakeEmail()
        with self.assertRaises(InterfaceError) as error:
            update_basics(self.db, basics)
        self.assertIn("unsupported type", str(error.exception))
