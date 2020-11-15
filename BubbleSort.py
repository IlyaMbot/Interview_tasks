#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:32:39 2020
"""


#import numpy as np
#sequence = np.random.randint(0,50,10)

sequence = [16, 37, 47, 21, 37, 35, 26, 46, 35, 30]
#s = [35, 29, 8, 18, 18, 10, 9, 11, 40, 47]


def bubble_sort(seq):
    count =0
    length = len(seq) - 1
    for j in range(length):
        for i in range(length - j):
            if seq[i] > seq[i + 1]:
                swap = seq[i + 1]
                seq[i + 1] = seq[i]
                seq[i] = swap
            count += 1
            print(seq)
    print(count)
    return(seq)

    
#print(sequence)
#bubble_sort(s)
bubble_sort(sequence)