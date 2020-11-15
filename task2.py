#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:13:22 2020

@author: conpucter
"""

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10] 
sequence2 = [6, 1, -1, 10] #for checking


def sequence_searcher(array, sequence):
    count = 0
    seq2 = []
    for i in sequence:
        for j in array[count:]:
            count += 1
            if i == j:
                seq2.append(j)
                break
    
    print(seq2, "\n", sequence, "\n", seq2 == sequence)
    
sequence_searcher(array, sequence) #this one must print TRUE
sequence_searcher(array, sequence2) #this one - FALSE