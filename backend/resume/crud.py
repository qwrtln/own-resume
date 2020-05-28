from sqlalchemy.orm import Session

from basics.crud import get_basics
from resume.schema import Resume
from work.crud import get_all_work


def create_resume(db: Session) -> Resume:
    db_basics = get_basics(db)
    db_work = get_all_work(db)
    return Resume(basics=db_basics, work=db_work)
