from typing import List

from sqlalchemy.orm import Session

from work.model import WorkModel
from work.schema import Work


def get_work_by_company(db: Session, company: str) -> WorkModel:
    return db.query(WorkModel).filter(WorkModel.company == company).first()


def get_all_work(db: Session) -> List[WorkModel]:
    return db.query(WorkModel).all()


def create_work_item(db: Session, work: Work) -> WorkModel:
    db_work = WorkModel(**work.dict())
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work


def update_work_item(db: Session, work: Work) -> WorkModel:
    db_work = get_work_by_company(db, work.company)
    db_work.company = work.company
    db_work.position = work.position
    db_work.summary = work.summary
    db.commit()
    return db_work


def delete_work_item(db: Session, work: Work) -> None:
    db.delete(work)
    db.commit()
