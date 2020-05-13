from db import db
from models import WorkModel

from .base import TestModelBase


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

    def test_jsonifying(self):
        basics = WorkModel(*list(self.work_1.values()))
        assert basics.json() == self.work_1

    def test_fetching_empty_works_list(self):
        fetched = WorkModel.fetch_all()

        assert len(fetched) == 0

    def test_fetching_single_workplace(self):
        self.givenWorkplace(self.work_1)

        fetched = WorkModel.fetch_all()

        assert isinstance(fetched, list)
        assert fetched[0].company == self.work_1.get("company")
        assert fetched[0].position == self.work_1.get("position")
        assert fetched[0].summary == self.work_1.get("summary")

    def test_fetching_multiple_workplaces(self):
        self.givenWorkplace(self.work_1)
        self.givenWorkplace(self.work_2)

        fetched = WorkModel.fetch_all()

        assert isinstance(fetched, list)
        assert len(fetched) == 2

    def test_fetching_by_company(self):
        self.givenWorkplace(self.work_1)
        self.givenWorkplace(self.work_2)

        fetched = WorkModel.find_by_company("company2")

        assert isinstance(fetched, WorkModel)
        assert fetched.summary == self.work_2.get("summary")

    def test_empty_result_for_fetching_by_company(self):
        self.givenWorkplace(self.work_1)

        fetched = WorkModel.find_by_company("company2")

        assert fetched is None

    def test_deleting_workplace(self):
        workplace = self.givenWorkplace(self.work_1)

        workplace.delete_from_db()

        assert workplace not in db.session

    def test_modifying_workplace(self):
        workplace = self.givenWorkplace(self.work_1)

        workplace.summary = "new summary"
        workplace.save_to_db()

        fetched = WorkModel.fetch_all()

        assert len(fetched) == 1
        assert fetched[0].summary == "new summary"

    def givenWorkplace(self, work):
        workplace = WorkModel(*list(work.values()))
        workplace.save_to_db()
        return workplace
