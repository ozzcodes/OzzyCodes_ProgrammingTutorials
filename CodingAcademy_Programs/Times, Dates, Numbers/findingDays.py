#!/usr/bin/python3
import calendar

cal = calendar.Calendar(0)
month = cal.monthdatescalendar(2019, 1)
lastWeek = month[-1]

print('Last Monday', lastWeek[0])  # Finds the date for the last Monday of month
print('Last Wednesday', lastWeek[2])  # Finds the date for the last Wednesday of month
