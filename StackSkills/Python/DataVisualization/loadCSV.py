# -*- coding: utf-8 -*-
# !/usr/bin/python3

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('myData.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Data Tutorial')

plt.show()
