from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from app import app


db = SQLAlchemy()


class TestResourceBase(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tests/fixtures/test_data.db"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.init_app(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
