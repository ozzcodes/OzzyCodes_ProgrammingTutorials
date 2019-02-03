import calendar

# sep = calendar.TextCalendar(calendar.SUNDAY)
# sep.prmonth(2018, 9)
#
# birthday = calendar.TextCalendar(calendar.MONDAY)
# birthday.prmonth(1990, 9)
#
#
# leaps = calendar.leapdays(1900, 2019)
# print(leaps)

# Create own calendar with user entry
print('>>>>>>>>>>Leap Year '
      'Calculator<<<<<<<<<<\n')
y1 = int(input("Enter the first year: "))
y2 = int(input("Enter the second year: "))

leaps = calendar.leapdays(y1, y2)
print("Number of leap years between", y1, "and", y2,
      "is", leaps)

