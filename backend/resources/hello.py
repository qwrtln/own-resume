from typing import Tuple

from flask import request
from flask_restful import Resource


class Hello(Resource):
    def get(self) -> Tuple[str, int]:
        ua = request.user_agent
        if all([ua.browser, ua.version, ua.platform]):  # type: ignore
            return (
                f"Hello, {ua.browser.capitalize()} {ua.version.split('.')[0]} on {ua.platform.capitalize()}!",  # type: ignore
                200,
            )
        return "Hello, mysterious user!", 200
