import pymongo
import os


def getDatabase():
<<<<<<< Updated upstream
    CONNECTION_STRING = "" #Use env variable to get URI string
=======
    CONNECTION_STRING = os.getenv('URI')
>>>>>>> Stashed changes

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['Capstone']

if __name__ == "__main__":
    dbname = getDatabase()
