import pytest

from tests.base import TestBase
from work.crud import (
    create_work_item,
    delete_work_item,
    get_all_work,
    get_work_by_company,
    update_work_item,
)
from work.model import WorkModel
from work.schema import Work


class WorkMixin:
    work_1 = {
        "company": "Gooooogl",
        "position": "Private data administrator",
        "summary": "I know everything about you now",
    }

    work_2 = {
        "company": "company2",
        "position": "position2",
        "summary": "summary2",
    }


@pytest.mark.crud
class TestWorkCrud(TestBase, WorkMixin):
    def test_get_by_company(self):
        work = get_work_by_company(self.db, "Żółć")
        self.assertIsInstance(work, WorkModel)

    def test_get_nonexistent_company(self):
        work = get_work_by_company(self.db, "Does not exist!")
        self.assertIsNone(work)

    def test_create_work(self):
        work = Work(**self.work_1)
        db_work = create_work_item(self.db, work)
        self.assertIn(db_work, self.db)
        self.assertIsInstance(db_work, WorkModel)

    def test_get_multiple_workplaces(self):
        works = get_all_work(self.db)
        self.assertEqual(len(works), 2)
        _ = create_work_item(self.db, Work(**self.work_1))
        _ = create_work_item(self.db, Work(**self.work_2))
        works = get_all_work(self.db)
        self.assertEqual(len(works), 4)

    def test_delete_work(self):
        work = get_work_by_company(self.db, "Corpo")
        delete_work_item(self.db, work)
        self.assertNotIn(work, self.db)

    def test_modify_workplace(self):
        changed_work = Work(**self.work_1)
        old_work = create_work_item(self.db, changed_work)
        changed_work.summary = "Changes!"
        db_work = update_work_item(self.db, changed_work)
        self.assertEqual(db_work.summary, "Changes!")
        self.assertEqual(old_work.company, changed_work.company)
        self.assertEqual(old_work.position, changed_work.position)
