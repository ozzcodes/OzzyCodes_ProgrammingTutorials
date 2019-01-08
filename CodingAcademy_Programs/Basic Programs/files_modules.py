#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:02:03 2018

@author: ozzycodes
"""

import os

f = open(os.environ["HOME"]+"/list.txt", "r")
f.readline()
f.readlines()
f.read()

f.close()
