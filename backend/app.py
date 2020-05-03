from flask import Flask
from flask_restful import Api

from resources import Hello, Resume

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, "/api/hello")
api.add_resource(Resume, "/api/resume")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
