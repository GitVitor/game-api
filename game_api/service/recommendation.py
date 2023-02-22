from game_api.repository.recommendation import RecommendationRepository


class RecommendationService():
    def __init__(self):
        self.recommendationRepository = RecommendationRepository()

    def find_all(self):
        return self.recommendationRepository.find_all()
    
    def find_by_id(self, id):
        return self.recommendationRepository.find_by_id(id)
