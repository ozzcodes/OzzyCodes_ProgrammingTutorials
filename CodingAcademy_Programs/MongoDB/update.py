#!/usr/bin/python3
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a collection
someData = db.someData
for document in someData.find():
    print(document)

for doc in someData.find({"code": {"$gt": 30}}).sort("n"):
    print(doc)

# Choosing a Document
print(someData.find_one({"n": 1}))

# Update it
someData.update({"n": 1}, {'$set': {'newField': 10}})

# Print again
print(someData.find_one({'newField': 10}))
