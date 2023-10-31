import pymongo


def getDatabase():
    CONNECTION_STRING = "mongodb+srv://BCSBruh:Dogman26@blog.yzwaere.mongodb.net/"

    client = pymongo.MongoClient(CONNECTION_STRING)
    return client['Capstone']

if __name__ == "__main__":
    dbname = getDatabase()
