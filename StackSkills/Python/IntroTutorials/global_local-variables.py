#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:11:48 2019

@author: ozzycodes
"""

# StakcSkills: Global and Local Variables

x = 6  # usually no need to globalize variables


def example3():
    global x
    x += 1
    print(x)


example3()


def example():
    z = 5
    print(z)

# cannot do this:
# print(z)

# Best Practice - Example2


def example2():
    z = 7
    print(z)

# cannot do (trying to modify global variable locally):
#    x += 1
#    print(x)

# can do:
    y = x + 1
    print(y)
    return y


x = example2()
print(x)
