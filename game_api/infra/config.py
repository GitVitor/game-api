import os

class Config:
    """
    Config class must be used to set environment variables for the project.
    For the correct usage set variables on your Local Environment or on Container Environment before start the API.
    """
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_URI = "mongodb+srv://%s:%s@%s/game?retryWrites=true&w=majority" % (MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST)