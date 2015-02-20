from bson import json_util

from mongo_json_encoder import *


class AccessObject():
    def __init__(self, db, collection_name):
        self._create_collection(db, collection_name)
        self.collection = db[collection_name]

    @staticmethod
    def _create_collection(db, collection_name):
        if collection_name not in db.collection_names(False):
            db.create_collection(collection_name)

    @staticmethod
    def _wrap_cursor(cursor):
        return [json.dumps(doc, default=json_util.default, cls=MongoJsonEncoder) for doc in cursor]

    def find_all(self):
        return self._wrap_cursor(self.collection.find())

    def find_range(self, skip, limit):
        return self._wrap_cursor(self.collection.find(skip=skip, limit=limit))

    def size(self):
        return self.collection.count()

    def save(self, doc):
        return self.collection.save(doc)
