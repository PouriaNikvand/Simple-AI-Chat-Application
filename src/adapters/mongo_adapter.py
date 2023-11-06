import pymongo
from pymongo import MongoClient


class BaseMongoClient:
    def __init__(self, host, db_name, coll_name):
        self.host = host
        self.db_name = db_name
        self.coll_name = coll_name
        self.client = MongoClient(self.host)
        self.db = self.client.get_database(self.db_name)
        self.coll = self.db[coll_name]

    def insert_one(self, doc):
        self.coll.insert_one(doc)

    def find_one(self, name, doc):
        query = {name: doc}
        sort = [("timestamp", pymongo.DESCENDING)]
        self.coll.find_one(query, sort=sort)

    def find(self, name, doc: str):
        query = {name: doc}
        sort = [("_id", pymongo.DESCENDING)]
        self.coll.find(query, sort=sort)

    def delete_one(self, name, doc_id):
        query = {name: doc_id}
        self.coll.delete_one(query)


class InteractionsMongoClient(BaseMongoClient):
    def get_user_interactions(self, user_id: str):
        return self.find("user_id", user_id)


class MessagesMongoClient(BaseMongoClient):
    def get_messages(self, interaction_id):
        return self.find("interaction_id", interaction_id)
