from typing import List

from pydantic import BaseModel


class WorkBase(BaseModel):
    company: str
    position: str
    summary: str = None


class WorkCreate(WorkBase):
    pass


class Work(WorkBase):
    class Config:
        orm_mode = True


class BasicsBase(BaseModel):
    name: str
    summary: str = None
    email: str = None


class BasicsCreate(BasicsBase):
    pass


class Basics(BasicsBase):
    class Config:
        orm_mode = True


class Resume(BaseModel):
    basics: Basics
    work: List[Work]
