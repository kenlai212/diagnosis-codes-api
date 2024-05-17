import pymongo

try:
    mongoClient = pymongo.MongoClient("mongodb+srv://ken:Maxsteel1596@cluster0.nvszeqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
except:
    print("Could not connect to MongoDB")

database = mongoClient["diagnosis_codes"]

codesCollection = database["codes"]
    
def saveCode(code):
    result = codesCollection.insert_one(code)
    return result.inserted_id


def getCodes():
    return codesCollection.find({})


def searchSimilar(searchVector):
    result = codesCollection.aggregate([
        {
            "$vectorSearch":{
                "index":"default",
                "path":"embedding",
                "queryVector":searchVector,
                "numCandidates":150,
                "limit":10
            }
        },
        {"$project": {"_id": 0, "diagnosisCode":1, "longDesc":1, "score": {"$meta": "vectorSearchScore"}}},
    ])

    return result


def deleteAllCodes():
    codesCollection.delete_many({})