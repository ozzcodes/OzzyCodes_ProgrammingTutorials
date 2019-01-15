#!/usr/bin/python3
import numpy
import scipy
from numpy import *
from scipy import constants, special

# Numpy version and Example
print(numpy.version.version)

a = array([1, 2, 3, 4, 5])
b = array([1, 0, -1, 0, -1])
print(a * 4)
print(4 + a)
print(sin(a))


# SciPy version and Example
print(scipy.version.version)

print(constants.c)
print(special.gamma(1))
print(special.gamma(-10))
