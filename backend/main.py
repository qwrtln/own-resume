from typing import Optional

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from models import crud, schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db() -> Optional[SessionLocal]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/resume", response_model=schemas.Resume)
def get_resume(db: Session = Depends(get_db)) -> schemas.Resume:
    db_basics = crud.get_basics(db)
    db_work = crud.get_all_work(db)
    return crud.create_resume(db_basics, db_work)
