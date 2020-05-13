import pytest

from db import db
from models import WorkModel

from .base import TestModelBase


@pytest.mark.model
class TestWork(TestModelBase):
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

    def given_workplace(self, work):
        workplace = WorkModel(**work)
        workplace.save_to_db()
        return workplace

    def test_jsonifying(self):
        work = WorkModel(**self.work_1)
        assert work.json() == self.work_1

    def test_fetching_empty_works_list(self):
        fetched = WorkModel.fetch_all()
        assert len(fetched) == 0

    def test_fetching_single_workplace(self):
        self.given_workplace(self.work_1)

        fetched = WorkModel.fetch_all()
        workplace = fetched[0]

        assert isinstance(fetched, list)
        assert workplace.company == self.work_1["company"]
        assert workplace.position == self.work_1["position"]
        assert workplace.summary == self.work_1["summary"]

    def test_fetching_multiple_workplaces(self):
        self.given_workplace(self.work_1)
        self.given_workplace(self.work_2)

        fetched = WorkModel.fetch_all()

        assert len(fetched) == 2

    def test_fetching_by_company(self):
        self.given_workplace(self.work_1)
        self.given_workplace(self.work_2)

        fetched = WorkModel.find_by_company("company2")

        assert isinstance(fetched, WorkModel)
        assert fetched.summary == self.work_2["summary"]

    def test_empty_result_for_fetching_by_company(self):
        self.given_workplace(self.work_1)

        fetched = WorkModel.find_by_company("company2")

        assert fetched is None

    def test_deleting_workplace(self):
        workplace = self.given_workplace(self.work_1)

        workplace.delete_from_db()

        assert workplace not in db.session

    def test_modifying_workplace(self):
        workplace = self.given_workplace(self.work_1)

        workplace.summary = "new summary"
        workplace.save_to_db()

        fetched = WorkModel.fetch_all()

        assert len(fetched) == 1
        assert fetched[0].summary == "new summary"
