from flask import Flask
from flask_restful import Api

from api.database import init_db
from api.resources.results import ResultsListAPI, ResultsAPI

@app.route('/')
def hello():
  return 'hello world'

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.Config')
    hello()

    init_db(app)

    api = Api(app)
    api.add_resource(ResultsListAPI, '/results')
    api.add_resource(ResultsAPI, '/results/<id>')

app = create_app()