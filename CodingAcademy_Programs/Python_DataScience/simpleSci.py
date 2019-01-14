#!/usr/bin/python3
from scipy.optimize import curve_fit
import numpy
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def line(x, a, b):
    return a * x + b


x = numpy.random.uniform(0., 100., 100)
y = 2. * x + 3. + numpy.random.normal(0., 10., 100)
plt.plot(x, y, '.')
plt.title('Drawing with SciPy', color='blue', family='monospace', fontweight='bold')
plt.xlabel('X value', family='monospace')
plt.ylabel('Y value', family='monospace')

error = numpy.repeat(10., 100)
popt, pcov = curve_fit(line, x, y, sigma=error)
print(popt)

xvalues = numpy.linspace(0., 100., 100)
plt.plot(xvalues, line(xvalues, popt[0], popt[1]), 'r-')
plt.savefig('scipyDraw.eps', format='eps', dpi=1000)
plt.show()
plt.close()
