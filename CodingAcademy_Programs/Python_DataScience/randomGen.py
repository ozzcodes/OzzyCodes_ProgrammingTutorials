#!/usr/bin/python3
import sys
import random

MIN = -1000
MAX = 20000
TOTAL = 100

for i in range(0, TOTAL):
    sys.stdout.write("%d\n" % random.randrange(MIN, MAX))
print()

# Pick random number from elements of a list
aList = [0, 1, -1, 2, -2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(aList))
print(random.sample(aList, 2))
print(random.shuffle(aList))
print(aList)
