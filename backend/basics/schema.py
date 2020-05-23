from pydantic import BaseModel


class BasicsBase(BaseModel):
    name: str
    summary: str = None
    email: str = None


class BasicsCreate(BasicsBase):
    pass


class Basics(BasicsBase):
    class Config:
        orm_mode = True
