from Modules import myModule
import sys
import numpy

if '/a/path' not in sys.path:
    sys.path.insert(0, '/a/path')

myModule.hello()
print(myModule.myVersion)

# each module has a file variable which is held in a relative path that 'numpy' can print out
print(numpy.__file__)
