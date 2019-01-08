"""
Python NAMESPACES are:
    - technique for generating containers that map
    names to an object
    - allow you to use the same function, variable or class
    multiple times without causing any problems
"""

# need to use 'global' function to tell new function to grab value from global variable

aGlobal = 1


def aFunction():
    global aGlobal
    aGlobal = aGlobal + 1
    print(aGlobal)


aFunction()
print(aGlobal)
