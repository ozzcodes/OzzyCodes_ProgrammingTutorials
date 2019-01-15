#!/usr/bin/python3
import numpy

# Using Numpy to create arrays an matrices
myArray = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray.min())
print(myArray.max())


# Matrices using NumPy
m1 = numpy.matrix('1 2 3; -1 -2 -3; -1 0 1')
m2 = numpy.matrix('0 2 3; -2 0 -3; -1 0 0')
print(m1.shape)
