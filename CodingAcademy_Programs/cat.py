#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 23:26:24 2018

@author: ozzycodes
"""

# Create own version of the UNIX function 'cat'
import sys
from optparse import OptionParser


# Class defining variables available to the cat command
class CatCommand:
    def __init__(self):
        self.count = 1

    def run(self, i, options):
        # sets default options
        e = ""

        for line in i:
            # modify printed line according to the option
            if options.showend:
                line = line.rstrip
                e = "$\n"

                if options.shownum:
                    line = "{0} {1}".format(self.count, line)

                self.count += 1
                print(line, end=e)


def main():
    usage = "usage: %prog [OPTION]... [FILE]..."
    parser = OptionParser(usage=usage)
    parser.add_option("-E", dest="showend", action="store_true", help="Show $ at line endings")
    parser.add_option("-n", dest="shownum", action="store_true", help="Show line numbers")
    (options, args) = parser.parse_args()

    c = CatCommand()

    if len(args) > 1:
        for a in args:
            f = open(a, "r")
            c.run(f, options)

    # otherwise use the stdin
    else:
        c.run(sys.stdin, options)


if __name__ == "__main__":
    main()

"""
# Simple, single argument function of cat.py to read a single file:

file = open(sys.argv[1], "r")
for line in fileinput.input():
    print(line, end="")
"""
