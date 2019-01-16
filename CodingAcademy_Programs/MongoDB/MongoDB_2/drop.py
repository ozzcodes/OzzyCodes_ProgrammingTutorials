from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client.LXF

# Choose a collection
moreData = db.moreData

# Drop the collection!
print moreData.drop()

print moreData.drop()