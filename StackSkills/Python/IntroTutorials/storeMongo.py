#!/usr/bin/python3

import sys
import pymongo
import re

total = 0
connMongo = pymongo.Connection('mongodb://localhost:27017')
db = connMongo.LXF
logs = db.aSite

for line in sys.stdin:
    line = line.rstrip('\n')
    parsed = list(map(''.join, re.findall(r'\"(.*?)\"/\[(.*?)\]|(\S+)', line)))
    total = total + 1
    log = {
        'host': parsed[0],
        'date': parsed[3],
        'document': parsed[4],
        'StatusCode': parsed[5],
        'size': parsed[6]
    }
    log_id = logs.insert(log)
    print('The _id of the interested post is', log_id)

connMongo.close()
print('Processed', total, 'log records!')
