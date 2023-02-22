from flask import Flask
from flask_restful import Api
from game_api.controller import recommendation
from game_api.infra.config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(recommendation.RecommendationList, '/recommendation')
api.add_resource(recommendation.Recommendation, '/recommendation/<string:id>')
