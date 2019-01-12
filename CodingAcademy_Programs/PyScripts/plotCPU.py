#!/usr/bin/pyhton3

import psutil
import matplotlib

matplotlib.get_backend()
matplotlib.use('Agg')

import matplotlib.pyplot as plt

x = []
y = []

for k in range(50):
    x.append(k)
    temp = psutil.cpu_percent(interval = 6)
    y.append(temp)

plt.ylabel('CPU Usage', family = 'monospace')
plt.plot(x, y)
plt.savefig('CPUplot.png')
plt.show()
plt.close()
