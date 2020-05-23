from typing import Optional

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from basics.crud import get_basics
from database import SessionLocal, engine, Base
from resume.crud import create_resume
from resume.schema import Resume
from work.crud import get_all_work


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db() -> Optional[SessionLocal]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/resume", response_model=Resume)
def get_resume(db: Session = Depends(get_db)) -> Resume:
    db_basics = get_basics(db)
    db_work = get_all_work(db)
    return create_resume(db_basics, db_work)
