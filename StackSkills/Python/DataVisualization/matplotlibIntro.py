#!/usr/bin/python3

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 7, 1, 9, 0]
y2 = [7, 2, 8, 1, 3]

"""
# Creates a plot with list of point [x],[y]
plt.plot(x, y)
"""

# Plot multiple plots with labels
plt.plot(x, y, label='Initial Line')
plt.plot(x, y2, label='New Line!')

# Label X-axis
plt.xlabel('Plot Number')

# Label Y-axis
plt.ylabel('Random Number')

# Graph Title
plt.title('Epic Graph tutorials with Python Matplotlib')

# Show the legends
plt.legend()

# Prints out the plotted graph
plt.show()
