from typing import List

from pydantic import BaseModel

from basics.schema import Basics
from work.schema import Work


class Resume(BaseModel):
    basics: Basics
    work: List[Work]
