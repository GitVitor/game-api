from flask import Flask
from flask_restful import Api
from game_api.controller import recommendation
from game_api.infra.config import Config
from game_api.infra.database import setup_database
from game_api.helpers import JSONEncoder

app = Flask(__name__)
app.config.from_object(Config) # LOAD ENVIRONMENT VARIABLES
app.json_encoder = JSONEncoder

with app.app_context():
  setup_database()

api = Api(app)

api.add_resource(recommendation.RecommendationList, '/recommendation')
api.add_resource(recommendation.Recommendation, '/recommendation/<string:id>')
