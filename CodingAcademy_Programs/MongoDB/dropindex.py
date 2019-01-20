#!/usr/bin/python3
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a Collection
someData = db.someData

# Drop and Index!
someData.drop_index("n_1")
