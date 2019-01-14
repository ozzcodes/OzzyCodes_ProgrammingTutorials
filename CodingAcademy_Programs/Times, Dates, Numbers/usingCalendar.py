#!/usr/bin/python3

import calendar

# Plain Text
textCalendar = calendar.TextCalendar(calendar.MONDAY)
textCalendar.prmonth(2019, 1)
textCalendar = calendar.TextCalendar(calendar.SUNDAY)
print(textCalendar.formatyear(2019, 2, 1, 1, 4))

# HTML Output
htmlCalendar = calendar.HTMLCalendar(calendar.MONDAY)
print(htmlCalendar.formatmonth(2016, 10, withyear=True))
# print(htmlCalendar.formatyear(2019, width=3))
