from pymongo import MongoClient
client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a collection
someData = db.someData

# Choose a document.
print someData.find_one({"n" : 1})
# Update it
someData.update({"n" : 1}, {'$set':{'newField': 10}})
# Print it again.
print someData.find_one({'newField': 10})
