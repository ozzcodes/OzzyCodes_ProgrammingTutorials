# -*- coding: utf-8 -*-
# !/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('myData.txt', delimiter=',', unpack=True)


# Simple example definition
def simple():
    return 5, 8


i, u = simple()

plt.plot(x, y, label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Data Tutorial')

plt.show()
