from typing import Any, Dict, Tuple

from flask_restful import Resource


from models import BasicsModel, WorkModel


class Resume(Resource):
    def get(self) -> Tuple[Dict[str, Any], int]:
        basics = BasicsModel.fetch().json()
        work_list = [work.json() for work in WorkModel.fetch_all()]
        return {"basics": basics, "work": work_list}, 200
