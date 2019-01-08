#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:10:54 2018

@author: ozzycodes
"""

## Example Code 1
# =============================================================================
# import math
# 
# def pythaga(a,b):
#     a2b2 = (a * a) + (b * b)
#     guess = 1.0
#     while(math.fabs((guess * guess) - a2b2) > 0.01):
#         guess = (((a2b2 / guess) + guess) / 2)
#     return guess
#
# print pythaga(2, 3)
# =============================================================================

import math


def square(x):
    return x * x


def sqrt(x, guess):
    def closeEnough(x, guess):
        if math.fabs(square(guess) - x) > 0.01:
            return True
        else:
            return False

    def improveGuess(x, guess):
        return (((x / guess) + guess) / 2)

    while closeEnough(x, guess):
        guess = improveGuess(x, guess)
    return guess


def pythaga(a, b):
    a2b2 = square(a) + square(b)
    return sqrt(a2b2, 1.0)


print(pythaga(2, 3))
