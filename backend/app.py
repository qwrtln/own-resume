import os

from flask import Flask
from flask_restful import Api

from db import db
from resources import Hello, Resume

LOCAL_DB_NAME = "data.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", f"sqlite:///{LOCAL_DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

api.add_resource(Hello, "/")
api.add_resource(Resume, "/resume")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
