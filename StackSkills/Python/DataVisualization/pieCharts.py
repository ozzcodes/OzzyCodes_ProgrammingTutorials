# -*- coding: utf-8 -*-
# !/usr/bin/python3

import matplotlib.pyplot as plt

# x variable is typically the 'amount/ totals'
labels = 'Taxes', 'Overhead', 'Entertainment'

sizes = [25, 32, 21]
colors = ['m', 'c', 'b']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, shadow=True, explode=(0, 0.1, 0),
        autopct='1.1f%%')
# Keeps the pie chart from displaying at an angle
plt.axis('equal')

plt.show()
