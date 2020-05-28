from sqlalchemy import Column, String

from database import Base


class WorkModel(Base):
    __tablename__ = "work"

    company = Column(String(80), primary_key=True)
    position = Column(String(80))
    summary = Column(String(360))
