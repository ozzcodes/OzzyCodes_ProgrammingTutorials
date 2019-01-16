from pymongo import MongoClient
client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a collection
someData = db.someData

for document in someData.find():
    print document

for doc in someData.find({"code": {"$gt": 30}}).sort("n"):
    print doc