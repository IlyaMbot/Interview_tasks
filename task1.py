#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:46:23 2020

@author: conpucter
"""
import numpy as np #better to use the python's random function instead of numpy

# the initial conditions:
#array = [3, 5, -4, 8, 11, 1, -1, 6]
#targetSum = 10

#Here I tried to set up some randomness
array = list(np.random.random_integers(-20, 20, size = 20))
targetSum = list(np.random.random_integers(-20, 20, size = 1))


def comparing_numbers(array):
    for i in array:
        for j in array:
            result = (i + j)
            if result == targetSum and i != j:
                print(i, j)

                
comparing_numbers(array)
print(targetSum)
        
