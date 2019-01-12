#!/usr/bin/python3

import sys

try:
    f = open('./text.txt')
    s = f.readline()
    s = s.rstrip('\n')
    print(s)
except IOError as e:
    errno, strerror = e.args
    print('I/O error({0}): {1}'.format(errno, strerror))
except:
    print('Unexpected Error: ', sys.exc_info()[0])
    raise