import pymongo
from pymongo import MongoClient


class BaseMongoClient:
    def __init__(self, connection_string, db_name, coll_name):
        self.connection_string = connection_string
        self.db_name = db_name
        self.coll_name = coll_name
        self.client = MongoClient(self.connection_string)
        self.db = self.client.get_database(self.db_name)
        self.coll = self.db[coll_name]

    def insert_one(self, doc):
        self.coll.insert_one(doc)

    def find_one(self, doc_id):
        query = {"id": doc_id}
        sort = [("timestamp", pymongo.DESCENDING)]
        self.coll.find_one(query, sort=sort)

    def find(self, doc_id):
        query = {"id": doc_id}
        sort = [("timestamp", pymongo.DESCENDING)]
        self.coll.find(query, sort=sort)

    def delete_one(self, doc_id):
        query = {"id": doc_id}
        self.coll.delete_one(query)
