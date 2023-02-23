from flask import current_app

class RecommendationRepository():
    def find_all(self):
        cursor = current_app._database.recommendation.find({})
        return list(cursor)

    def find_by_id(self, id):
        return {
            "id": id,
            "helpful": 0,
            "funny": 0,
            "date": "2022-12-12",
            "is_recommended": True,
            "hours": 36.3,
            "user_id": 14546,
            "review_id": 0
        }
