import redis
import sys

r = redis.StrictRedis(host='localhost', port=6379, db=0)

if len(sys.argv) != 4:
    print('Wrong number of arguments!')
    print('insert.py phone name surname')
    sys.exit(1)

telephone = sys.argv[1]
name = sys.argv[2]
surname = sys.argv[3]

myTel = r.rpush(telephone, telephone)
myName = r.rpush(telephone, name)
mySurname = r.rpush(telephone, surname)
