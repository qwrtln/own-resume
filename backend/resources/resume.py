from typing import Any, Dict, Tuple

from flask_restful import Resource


from models.work import WorkModel


resume = {
    "basics": {
        "name": "Bonawentura Kluczbork",
        "summary": "Pro Gram I Sta",
        "email": "proprietary@noneofyour.business",
    },
    "work": None
}


class Resume(Resource):
    def get(self) -> Tuple[Dict[str, Any], int]:
        works = [work.json() for work in WorkModel.fetch_all()]
        resume["work"] = works  # type: ignore
        return resume, 200
