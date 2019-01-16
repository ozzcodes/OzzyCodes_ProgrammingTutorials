import pymongo
from pymongo import MongoClient

from bottle import route, run, template

# Get data from MongoDB
myData = []
client = MongoClient('localhost', 27017)
db = client.LXF
cursor = db.sampleData.find({}, {'_id':0, 'y':0})

for myDoc in cursor:
    # print(myDoc)
    myData.append(myDoc['x'])

@route('/')
def rootDirectory():
    return template('listContents', data=myData)

run(host='localhost', port=1234)
