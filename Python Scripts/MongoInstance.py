import pymongo
import os


def getDatabase():
    CONNECTION_STRING = "mongodb+srv://Capstone:cExlM50d9QzkQFPY@capstone.h9p4nqr.mongodb.net/" #Use env variable to get URI string

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['Capstone']

if __name__ == "__main__":
    dbname = getDatabase()
