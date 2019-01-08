#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:59:41 2018

@author: ozzycodes
"""

# =============================================================================
# list=['banana','tiffin','burrito']
#  
#  
# for item in list:
#     print(item)
#      
# tm = open('timemachine.txt', 'r')
#  
# for line in tm:
#     print(line)
#  
# line.strip()
# line.split(' ')
# =============================================================================


tm = open('timemachine.txt', 'r')
for line in tm:
    line = line.strip()
    line = line.translate(None,'!"#$%^&*\'()+,"-./:;<=>?@[\\]_`{|}~')
    line = line.lower()
    list = line.split(' ')

dict={}
for word in list:
    dict[word] = 1

if word in dict:
    count = dict[word]
    count += 1
    dict[word] = count
else:
    dict[word] = 1

for word,count in dict.iteritems():
    print(word+": "+str(count))

