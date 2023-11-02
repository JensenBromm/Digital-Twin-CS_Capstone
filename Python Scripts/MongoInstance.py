import pymongo


def getDatabase():
    CONNECTION_STRING = "" #Use env variable to get URI string

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['Capstone']

if __name__ == "__main__":
    dbname = getDatabase()
