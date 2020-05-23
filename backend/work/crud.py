from typing import List

from sqlalchemy.orm import Session

from work.model import WorkModel
from work.schema import Work


def get_work_by_company(db: Session, company: str) -> WorkModel:
    return db.query(WorkModel).filter_by(WorkModel.company == company).first()


def get_all_work(db: Session) -> List[WorkModel]:
    return db.query(WorkModel).all()


def create_work_item(db: Session, work: Work, employee: str) -> WorkModel:
    db_work = WorkModel(**work.dict(), employee=employee)
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work
