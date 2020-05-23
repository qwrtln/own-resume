import json
import unittest

import pytest
from pydantic import ValidationError

from basics.crud import get_basics
from resume.crud import create_resume
from resume.schema import Resume
from work.crud import get_all_work

from tests.fixtures.test_db import get_testing_db
from tests.fixtures.test_resume import test_resume


@pytest.mark.crud
class TestResumeCrud(unittest.TestCase):
    def setUp(self):
        self.db = get_testing_db()

    def test_creation(self):
        basics = get_basics(self.db)
        work = get_all_work(self.db)
        resume = create_resume(basics, work)
        self.assertEqual(resume.json(), json.dumps(test_resume))

    def test_missing_basics_summary(self):
        basics = get_basics(self.db)
        delattr(basics, "summary")
        work = get_all_work(self.db)
        resume = create_resume(basics, work)
        self.assertIsNone(json.loads(resume.json())["basics"]["summary"])

    def test_missing_basics_name(self):
        basics = get_basics(self.db)
        del basics.name
        work = get_all_work(self.db)
        with self.assertRaises(ValidationError) as error:
            _ = create_resume(basics, work)
            self.assertEqual(error.value.model, Resume)
            self.assertEqual(
                error.value.errors()[0]["msg"], "none is not an allowed value"
            )

    def test_basics_email_wrong_type(self):
        basics = get_basics(self.db)

        class FakeEmail:
            pass

        basics.email = FakeEmail()
        work = get_all_work(self.db)
        with self.assertRaises(ValidationError) as error:
            _ = create_resume(basics, work)
            self.assertEqual(error.value.model, Resume)
            self.assertEqual(error.value.errors()[0]["msg"], "str type expected")
