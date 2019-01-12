import time
import datetime

'''
now = time()
print(now)

then = time()
timeDifference = then - now
print(timeDifference)

# print(minutes, seconds)

print('The difference is %.2f seconds' % timeDifference)
'''

# Time conversion
LocalTime = datetime.datetime.now()
print(LocalTime)

EpochSecond = time.mktime(LocalTime.timetuple())
print(EpochSecond)

utcTime = datetime.datetime.utcfromtimestamp(EpochSecond)
print(utcTime)

print(LocalTime.ctime())
print(utcTime.ctime())

