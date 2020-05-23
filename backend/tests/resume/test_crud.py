import json

import pytest
from pydantic import ValidationError

from basics.crud import get_basics
from resume.crud import create_resume
from resume.schema import Resume
from work.crud import get_all_work

from tests.fixtures.test_db import get_testing_db
from tests.fixtures.test_resume import test_resume


def test_creation():
    db = get_testing_db()
    basics = get_basics(db)
    work = get_all_work(db)
    resume = create_resume(basics, work)
    assert resume.json() == json.dumps(test_resume)


def test_missing_basics_summary():
    db = get_testing_db()
    basics = get_basics(db)
    delattr(basics, "summary")
    work = get_all_work(db)
    resume = create_resume(basics, work)
    assert json.loads(resume.json())["basics"]["summary"] is None


def test_missing_basics_name():
    db = get_testing_db()
    basics = get_basics(db)
    del basics.name
    work = get_all_work(db)
    with pytest.raises(ValidationError) as error:
        _ = create_resume(basics, work)
    assert error.value.model == Resume
    assert error.value.errors()[0]["msg"] == "none is not an allowed value"


def test_basics_email_wrong_type():
    db = get_testing_db()
    basics = get_basics(db)

    class Garbage:
        pass
    basics.email = Garbage()
    work = get_all_work(db)
    with pytest.raises(ValidationError) as error:
        _ = create_resume(basics, work)
    assert error.value.model == Resume
    assert error.value.errors()[0]["msg"] == "str type expected"
