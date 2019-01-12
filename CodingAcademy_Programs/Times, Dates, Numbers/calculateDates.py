from datetime import date
from datetime import timedelta
import calendar

today = date.today()
print(today)

# Find how many days are until Christmas
Christmas = date(2019, 12, 25)
print(Christmas - today)

# What will the date be in 90 days
print(today + timedelta(days=90))
print((today + timedelta(days=90)).weekday())

# Name of the day using calendar
dayIndex = (today + timedelta(days=90)).weekday()
print(calendar.day_name[dayIndex])

