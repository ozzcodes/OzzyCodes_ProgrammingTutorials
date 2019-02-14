#!/usr/bin/python3

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
x2 = [4, 5, 1, 6, 8]
y = [10, 7, 1, 9, 0]
y2 = [7, 2, 8, 1, 3]

# Designate graph as a bar graph
plt.bar(x, y, label="One", color='m')
plt.bar(x2, y2, label="Two", color='g')

plt.xlabel('Bar number')
plt.ylabel('Bar height')
plt.title('Bar Chart Title')

# Show the legends
plt.legend()

# Prints out the plotted graph
plt.show()
