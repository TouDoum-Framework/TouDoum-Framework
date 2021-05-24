import pymongo


class ResultManger:
    client: pymongo.MongoClient
    database = None
    collection = None

    def __init__(self):
        self.client = pymongo.MongoClient('127.0.0.1', 27017, username='please', password='change_me')
        self.database = self.client['TouDoum']
        self.collection = self.database['result']

    def save(self, data):
        print(str(data))