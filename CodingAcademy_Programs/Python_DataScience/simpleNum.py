#!/usr/bin/python3
import matplotlib
import numpy
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

values = numpy.linspace(-2 * numpy.pi, 2 * numpy.pi, 100)
plt.plot(numpy.cos(values))
plt.savefig('./numpyDraw.png')
plt.show()
plt.close()
