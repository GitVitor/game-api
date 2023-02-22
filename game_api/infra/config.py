import os

class Config:
    """
    Config class must be used to set environment variables for the project.
    For the correct usage set variables on your Local Environment or on Container Environment before start the API.
    """
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_URI = "mongodb+srv://%s:%s@%s/?retryWrites=true&w=majority" % (DB_USERNAME, DB_PASSWORD, DB_HOST)