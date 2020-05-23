from typing import List

from basics.model import BasicsModel
from resume.schema import Resume
from work.model import WorkModel


def create_resume(basics: BasicsModel, works: List[WorkModel]) -> Resume:
    return Resume(basics=basics, work=works)
