import pymongo

try:
    mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
except:
    print("Could not connect to MongoDB")

database = mongoClient["diagnosis_codes"]

codesCollection = database["codes"]

def saveCode(code):
    result = codesCollection.insert_one(code)
    return result.inserted_id

def getCodes():
    return codesCollection.find({})

def deleteAllCodes():
    codesCollection.delete_many({})