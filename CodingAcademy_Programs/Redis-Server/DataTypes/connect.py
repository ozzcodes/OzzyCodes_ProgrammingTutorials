import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
myVal = r.set('One', 'Two')

if myVal:
    print('Set operation was successful!')
else:
    print('Operation failed!')

myVal = r.get('One')
print('The value of One is: ' + myVal)
