#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:00:07 2020

@author: conpucter
"""
'''
this task is not done yet
this search doesn't work with extreme numbers like 0 and 73
'''

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 71

def array_keeper(array):
    print("array keeper i\'m calling you")
    
    
def binary_search(array, target):
    count = 0
    a = 0
    b = len(array) - 1
    while 1 == 1:
        position = (a + b)//2
        print(a, b, position)
        if array[position] > target:
            #print("number is larger than target")
            b -= position 
        elif array[position] < target:
            #print("number is smaller than target")
            a += position
        else:
            print(position)
            break
        count += 1
        if count == len(array):
            #kind of protection...
            print("ERROR: there\'s no such number or the array isn\'t sorted")
            break
        
binary_search(array, target)


