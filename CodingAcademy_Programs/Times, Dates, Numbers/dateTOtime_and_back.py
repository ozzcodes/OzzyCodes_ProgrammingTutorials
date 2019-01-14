from datetime import datetime

myString = '2019-01-14 00:42:25'
aDate = datetime.strptime(myString, "%Y-%m-%d %H:%M:%S")
print(type(aDate))

print(aDate.strftime('%Y'))
print(aDate.strftime('%Y-%m-%d'))
print(aDate.strftime('%d-%m-%Y'))
print(type(aDate.strftime('%d-%m-%Y')))
