from flask import current_app
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoConfig:
    @staticmethod
    def setup():
      db_password = ""
      db_username = ""
      db_host = ""
      db_uri = "mongodb+srv://%s:%s@%s/?retryWrites=true&w=majority" % (db_username, db_password, db_host)
      client = MongoClient(db_uri, server_api=ServerApi('1'))
      db = client.game

      return db

      