from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from resume.crud import create_resume
from resume.schema import Resume


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/resume", response_model=Resume)
def get_resume(db: Session = Depends(get_db)) -> Resume:
    return create_resume(db)
