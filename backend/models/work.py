from __future__ import annotations

from typing import Dict, List, Optional

from db import db


class WorkModel(db.Model):
    __tablename__ = "work"

    company = db.Column(db.String(80), primary_key=True)
    position = db.Column(db.String(80))
    summary = db.Column(db.String(360))

    def __init__(self, company: str, position: str, summary: str) -> None:
        self.company = company
        self.position = position
        self.summary = summary

    def json(self) -> Dict[str, str]:
        return {
            "company": self.company,
            "position": self.position,
            "summary": self.summary,
        }

    @classmethod
    def find_by_company(cls, company: str) -> Optional[WorkModel]:
        return cls.query.filter_by(company=company).first()

    @classmethod
    def fetch_all(cls) -> Optional[List[WorkModel]]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
