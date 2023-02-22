from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import dumps, loads
from flask import current_app

db_password = "TM7uGqsJfhoU4HEs"
db_username = "vitorDev"
db_host = "cluster0.chqrg.mongodb.net"
db_uri = "mongodb+srv://%s:%s@%s/?retryWrites=true&w=majority" % (db_username, db_password, db_host)

client = MongoClient(db_uri, server_api=ServerApi('1'))
db = client.game

class RecommendationRepository():
    def find_all(self):
        config = current_app.config
        cursor = db.recommendation.find({})
        json_data = dumps(list(cursor), indent = 2) 
        return loads(json_data)

        # return json_data

        # recommendationsMock = [{
        #     "id": 975370,
        #     "helpful": 0,
        #     "funny": 0,
        #     "date": "2022-12-12",
        #     "is_recommended": True,
        #     "hours": 36.3,
        #     "user_id": 14546,
        #     "review_id": 0
        # }, {
        #     "id": 304390,
        #     "helpful": 4,
        #     "funny": 0,
        #     "date": "2017-02-17",
        #     "is_recommended": False,
        #     "hours": 11.5,
        #     "user_id": 797,
        #     "review_id": 1
        # }]
        # return recommendationsMock
    
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
