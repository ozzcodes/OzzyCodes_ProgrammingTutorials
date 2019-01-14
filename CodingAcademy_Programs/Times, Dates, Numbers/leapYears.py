#!/usr/bin/python3
import calendar
import sys


def isLeapYear(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False


''' 
Get command line arguments
and process them one by one
'''
for argument in sys.argv[1]:
    year = int(argument)
    if calendar.isleap(year):
        print(year, 'is leap year!')
