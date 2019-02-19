#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('mystyle')

# Matplotlib will eventually copy colors after 7 data lines
for label in range(8):
    x = []
    y = []

    for i in range(1, 10):
        ys = random.randrange(0, 15)
        xs = i
        x.append(xs)
        y.append(ys)

    plt.plot(x, y, label=label)

plt.legend()
plt.show()
