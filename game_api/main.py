from flask import Flask
from flask_restful import Api
from game_api.controller import recommendation

app = Flask(__name__)
api = Api(app)

api.add_resource(recommendation.RecommendationList, '/recommendation')
api.add_resource(recommendation.Recommendation, '/recommendation/<string:id>')

if __name__ == "__main__":
    print("server rodando")
    api.run(debug=True)