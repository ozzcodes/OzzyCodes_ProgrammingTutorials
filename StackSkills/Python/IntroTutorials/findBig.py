#!/usr/bin/python3

import os
import sys

if len(sys.argv) >= 2:
    directory = str(sys.argv[1])
else:
    print('Not enough arguments!')
    sys.exit(0)    
noBytes = 0

fileName = ''
for root, dirs, files in os.walk(directory):
    for file in files:
        pathname = os.path.join(root, file)
        if os.path.exists(pathname):
            if noBytes < os.path.getsize(pathname):
                noBytes = os.path.getsize(pathname)
                fileName = pathname

print(fileName)
print('Size: ', noBytes)