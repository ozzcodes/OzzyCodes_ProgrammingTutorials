import calendar

cal = open("cal.html", "w")
c = calendar.HTMLCalendar(calendar.SUNDAY)
cal.write(c.formatmonth(2019, 1))
cal.close()
