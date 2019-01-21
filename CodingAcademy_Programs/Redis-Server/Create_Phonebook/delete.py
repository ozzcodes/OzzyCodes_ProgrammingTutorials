import redis
import sys

if len(sys.argv) != 2:
    print('Wrong number of arguments!')
    print('delete.py phone')
    sys.exit(1)

r = redis.StrictRedis(host='localhost', port=6379, db=0)
telephone = sys.argv[1]
aList = r.delete(telephone)

if aList:
    print(aList)
else:
    print('Telephone number not found, cannot delete!')
