import datetime
import time

# Epoch Time
epochTime = 1547336376

newDateTimeObject = datetime.datetime.fromtimestamp(epochTime)
print(newDateTimeObject)
print(type(newDateTimeObject))
print(newDateTimeObject.timestamp())

myTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
print(myTime)
print(type(myTime))


# Time.struct_time Objects
myTime = time.gmtime()
print(type(myTime))
print(myTime)

print(time.strftime('%H:%M of %Y-%m-%d', myTime))
print(myTime[1])
print(myTime.tm_mon)
