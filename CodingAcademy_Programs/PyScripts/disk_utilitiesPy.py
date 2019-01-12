#!/usr/bin/python3
'''
Calculates the sizes of the subdirectories
that exists in a directoy
'''

import os
import sys

def directorySize(path):
    total = 0
    
    for entry in os.listdir(path):
        fullPath = os.path.abspath(os.path.join(path, entry))
        if os.path.isdir(fullPath):
            total += directorySize(fullPath)
        elif os.path.isfile(fullPath):
            total += os.path.getsize(fullPath)
    
    return total
    
if len(sys.argv) >= 2:
    directory = os.path.normpath(os.path.abspath((sys.argv[1])))
    print('\t\Start from: ', directory)
else:
    print('Not enough arguments!')
    sys.exit(0)

dirList = next(os.walk(directory))[1]
for current in dirList:
    current = os.path.join(directory, current)
    print('\tChecking: ', current)
    print(directorySize(path = current), 'bytes')