from typing import List

from sqlalchemy.orm import Session

from . import schemas
from .basics import BasicsModel
from .schemas import Resume
from .work import WorkModel


def get_basics(db: Session) -> BasicsModel:
    return db.query(BasicsModel).first()


def save_basics_to_db(db: Session, basics: schemas.Basics) -> BasicsModel:
    db_basics = BasicsModel(**basics.dict())
    db.add(db_basics)
    db.commit()
    db.refresh(db_basics)
    return db_basics


def get_work_by_company(db: Session, company: str) -> WorkModel:
    return db.query(WorkModel).filter_by(WorkModel.company == company).first()


def get_all_work(db: Session) -> List[WorkModel]:
    return db.query(WorkModel).all()


def create_work_item(db: Session, work: schemas.Work, employee: str) -> WorkModel:
    db_work = WorkModel(**work.dict(), employee=employee)
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work


def create_resume(basics: schemas.Basics, works: List[schemas.Work]) -> Resume:
    return Resume(basics=basics, work=works)
