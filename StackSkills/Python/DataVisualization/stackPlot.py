# -*- coding: utf-8 -*-
# !/usr/bin/python3

import matplotlib.pyplot as plt

year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# are in the thousands
taxes = [17, 18, 40, 43, 44, 8, 43, 32, 39, 30]
overhead = [20, 22, 9, 29, 17, 12, 14, 24, 49, 35]
entertainment = [41, 32, 27, 13, 19, 12, 22, 18, 28, 20]

plt.plot([], [], color='m', label='taxes')
plt.plot([], [], color='c', label='overhead')
plt.plot([], [], color='b', label='entertainment')

# Tough to label data types with legends to differentiate data
# so add something like a color type:
plt.stackplot(year, taxes, overhead, entertainment, colors=['m', 'c', 'b'])
plt.legend()
plt.title('Company Expenses')
plt.xlabel('Year')
plt.ylabel('Cost, in thousands')

plt.show()
