#!/usr/bin/python3
import numpy
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = numpy.linspace(-10, 10, 500)
y1 = x
y2 = x ** 2
y3 = x ** 3
y4 = x ** 4

f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y1)
axarr[0, 0].axhline(0, color='red')
axarr[0, 0].axvline(0, color='red')
axarr[0, 0].set_title('[0,0]')
axarr[0, 1].plot(x, y1)
axarr[0, 1].plot(x, y2)
axarr[0, 1].axhline(0, color='red')
axarr[0, 1].axvline(0, color='red')
axarr[0, 1].set_title('[0,1]')
axarr[1, 0].plot(x, y3)
axarr[1, 0].set_title('[1,0]')
axarr[1, 0].axhline(0, color='red')
axarr[1, 0].axvline(0, color='red')
axarr[1, 1].plot(x, y4)
axarr[1, 1].set_title('[1,1]')
axarr[1, 1].axhline(0, color='red')
axarr[1, 1].axhline(0, color='red')
plt.suptitle('Plotting multiple functions!', color='blue', family='monospace', fontweight='bold')
plt.savefig('multipleDraw.eps', format='eps', dpi=1000)
plt.show()
plt.close()
