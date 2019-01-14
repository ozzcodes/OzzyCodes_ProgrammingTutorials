#!/usr/bin/python3
import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
import sys

matplotlib.use('TkAgg')

if len(sys.argv) >= 2:
    filename = str(sys.argv[1])
else:
    print('Not enough arguments!')
    sys.exit(0)

x = np.empty(0)
y = np.empty(0)

# Read text file
try:
    f = open(filename, 'r')
except IOError as e:
    errno, sterror = e.args
    print('I/O error({0}): {1}'.format(errno, sterror))

for line in f:
    newLine = line.rstrip().split('\t')
    dateTimeObject = datetime.datetime.strptime(newLine[0], "%H:%M %Y-%m-%d")
    x = np.append(x, dateTimeObject)
    y = np.append(y, newLine[1])

plt.xlabel("Time of Day")
plt.ylabel("Value")
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.plot(x, y)
plt.savefig('./timeSeries.png', dpi=300)
plt.show()
plt.close()
