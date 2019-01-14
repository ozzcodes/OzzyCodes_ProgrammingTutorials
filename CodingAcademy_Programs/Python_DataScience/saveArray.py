#!/usr/bin/python3
import numpy

print(numpy.version.version)
# Storing arrays for later use
anArray = numpy.array([[1, 2, 3], [4, 5, 6]])
print('Existing array:\n', anArray)

numpy.save('usingSave.txt', anArray)
numpy.savetxt('usingSavetxt.txt', anArray)
loadArray = numpy.load('usingSave.txt.npy')
loadArraytxt = numpy.loadtxt('usingSavetxt.txt')

print('Using load()\n', loadArray)
print('Using loadtxt()\n', loadArraytxt)
