# -*- coding: utf-8 -*-
# !/usr/bin/python3

import matplotlib.pyplot as plt

# Create a list of data
test_scores = [92, 76, 77, 90, 85, 46, 99, 68, 77, 34, 56, 87, 65, 90, 100, 77, 78, 89]
time_spent = [20, 22, 15, 30, 35, 12, 29, 33, 55, 20, 60, 38, 30, 37, 12, 11, 15, 42]

plt.scatter(time_spent, test_scores)

# Axis and Graph Titles
plt.xlabel('Time spent on Test')
plt.ylabel('Test Scores')
plt.title('Test Scores vs Time Spent')

plt.show()

# Using Multiple Dataset for visual analysis (Example data)
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 2, 4, 2]
y2 = [8, 8, 6, 7, 6]

plt.scatter(x, y1, marker='o', color='c')
plt.scatter(x, y2, marker='v', color='m')

plt.show()
