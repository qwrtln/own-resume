from flask import Flask
from flask_restful import Api

from resources import Hello, Resume

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, "/")
api.add_resource(Resume, "/resume")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
