from flask import current_app
from flask_pymongo import PyMongo

def setup_database():
  """
  Configuration method to return db instance
  """
  client = PyMongo(current_app)

  current_app._database = getattr(current_app, "_database", None)

  if current_app._database is None:
    current_app._database = client.db
