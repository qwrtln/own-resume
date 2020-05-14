from __future__ import annotations

from typing import Dict

from db import db


class BasicsModel(db.Model):
    __tablename__ = "basics"

    name = db.Column(db.String(80), primary_key=True)
    summary = db.Column(db.String(360))
    email = db.Column(db.String(80))

    def __init__(self, name: str, summary: str, email: str) -> None:
        self.name = name
        self.summary = summary
        self.email = email

    def json(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "summary": self.summary,
            "email": self.email,
        }

    @classmethod
    def fetch(cls) -> BasicsModel:
        return cls.query.first()

    def save_to_db(self) -> None:
        self.query.delete()
        db.session.add(self)
        db.session.commit()
