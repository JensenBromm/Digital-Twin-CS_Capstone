from MongoInstance import getDatabase

dbname = getDatabase()
collection_name = dbname["robots"]

robotDict = {
    "_id" : "Robot 1",
    "x" : 0,
    "z" : 0
}
keyValue = {"_id" : robotDict["_id"]}
collection_name.update_one(keyValue, {"$set": robotDict}, upsert=True)

while robotDict["x"] != 5:
    robotDict["x"] += 0.0000001
    #print(robotDict["x"])
    collection_name.update_one(keyValue, {"$set": robotDict}, upsert=True)