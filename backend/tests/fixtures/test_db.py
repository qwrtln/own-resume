from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base

engine = create_engine(
    "sqlite:///./tests/fixtures/test_data.db", connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
