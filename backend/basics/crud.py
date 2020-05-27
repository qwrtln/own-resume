from sqlalchemy.orm import Session

from basics.model import BasicsModel
from basics.schema import Basics


def get_basics(db: Session) -> BasicsModel:
    return db.query(BasicsModel).first()


def save_basics_to_db(db: Session, basics: Basics) -> BasicsModel:
    db_basics = BasicsModel(**basics.dict())
    db.add(db_basics)
    db.commit()
    db.refresh(db_basics)
    return db_basics


def update_basics(db: Session, basics: Basics) -> BasicsModel:
    db_basics = get_basics(db)
    db_basics.name = basics.name
    db_basics.summary = basics.summary
    db_basics.email = basics.email
    db.commit()
    return db_basics
