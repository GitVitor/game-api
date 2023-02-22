from game_api.service.recommendation import RecommendationService
from flask_restful import Resource

class RecommendationList(Resource):
    def __init__(self):
        self.recommendationService = RecommendationService()

    def get(self):
        return self.recommendationService.find_all()


class Recommendation(Resource):
    def __init__(self):
        self.recommendationService = RecommendationService()

    def get(self, id):
        return self.recommendationService.find_by_id(id)