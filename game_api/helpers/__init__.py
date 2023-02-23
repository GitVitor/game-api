from bson.json_util import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    """A JSON encoder that uses :mod:`bson.json_util` for MongoDB documents."""
    def default(self, obj):
      if isinstance(obj, ObjectId):
          return str(obj)
      return super(JSONEncoder, self).default(obj)
