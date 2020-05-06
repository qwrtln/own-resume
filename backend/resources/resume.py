from typing import Any, Dict, Tuple

from flask_restful import Resource

resume = {
    "basics": {
        "name": "Bonawentura Kluczbork",
        "summary": "Pro Gram I Sta",
        "email": "proprietary@noneofyour.business",
    },
    "work": [
        {
            "company": "Żółć",
            "position": "Go Developer",
            "summary": "We produced dictionaries!",
        },
        {
            "company": "Corpo",
            "position": "Super Señor Developer",
            "summary": "I made magic.",
        },
    ],
}


class Resume(Resource):
    def get(self) -> Tuple[Dict[str, Any], int]:
        return resume, 200
