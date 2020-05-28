import json

import pytest

from basics.crud import get_basics, update_basics
from resume.crud import create_resume
from tests.base import TestBase

from tests.fixtures.test_resume import test_resume


@pytest.mark.crud
class TestResumeCrud(TestBase):
    def test_creation(self):
        resume = create_resume(self.db)
        self.assertEqual(resume.json(), json.dumps(test_resume))

    def test_missing_basics_summary(self):
        basics = get_basics(self.db)
        delattr(basics, "summary")
        update_basics(self.db, basics)
        resume = create_resume(self.db)
        self.assertIsNone(json.loads(resume.json())["basics"]["summary"])
