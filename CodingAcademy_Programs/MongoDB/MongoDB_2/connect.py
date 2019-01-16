from pymongo import MongoClient
client = MongoClient("127.0.0.1", 27017)

db = client.LXF

# Choose a collection
sampleData = db.sampleData

item = sampleData.find_one()
print item['_id']
print item['x']
