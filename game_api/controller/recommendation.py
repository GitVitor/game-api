from game_api.service.recommendation import RecommendationService
from flask_restful import Resource
from flask import jsonify

class RecommendationList(Resource):
    def __init__(self):
        self.recommendationService = RecommendationService()

    def get(self):
        data = self.recommendationService.find_all()
        data_json = jsonify(data)
        return data_json


class Recommendation(Resource):
    def __init__(self):
        self.recommendationService = RecommendationService()

    def get(self, id):
        return self.recommendationService.find_by_id(id)