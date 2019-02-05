#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:30:06 2019

@author: ozzycodes
"""

# StakcSkills: Functions tutorial

def example():
    x = 1
    y = 3
    
    print(x + y)
    
    if x < y:
        print(x,'is less than', y)
    else:
        print('nothing to be done')

def main():
    example()


# Functions and Parameters

def addition(num1, num2, num3, num4):
    answer = num1 + num2 + num3 + num4
    return answer

x = addition(5, 6, 6, 5)
print(x)

# applying default parameters so no need for complete customization
def website(font='TNR',
        background_color='white',
        font_size='11',
        font_color='black'):
    print('Font:', font)
    print('BG:', background_color)
    print('Font size:', font_size)
    print('Font color:', font_color)

# website('TNR','white','11','black')

#website(font='TNR',
 #       background_color='white',
  #      font_size='11',
   #     font_color='black')

# website()

website(background_color = 'grey')