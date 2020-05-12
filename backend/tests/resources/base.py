import pytest

from flask_sqlalchemy import SQLAlchemy

from app import app


db = SQLAlchemy()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///tests/fixtures/test_data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.test_client() as client:
        yield client
