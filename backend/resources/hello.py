from typing import Tuple

from flask_restful import Resource


class Hello(Resource):
    def get(self) -> Tuple[str, int]:
        return "Hello, World!", 200
