from sqlalchemy import Column, String

from database import Base


class BasicsModel(Base):
    __tablename__ = "basics"

    name = Column(String(80), primary_key=True)
    summary = Column(String(360))
    email = Column(String(80))
