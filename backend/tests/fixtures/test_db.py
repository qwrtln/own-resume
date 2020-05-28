from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base

DB_FILE = "./tests/fixtures/test_data.db"

engine = create_engine(
    f"sqlite:///{DB_FILE}", connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    transaction = db.begin(subtransactions=True)
    try:
        yield db
    finally:
        transaction.rollback()
        db.close()


def get_testing_db():
    return next(override_get_db())
