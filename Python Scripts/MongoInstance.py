import pymongo
import os


def getDatabase():
    CONNECTION_STRING = os.getenv('URI')

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['Capstone']

if __name__ == "__main__":
    dbname = getDatabase()
