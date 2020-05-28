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
