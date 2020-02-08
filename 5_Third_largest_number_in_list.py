#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:51:34 2020

@author: mharesam
"""

def remove_largest (x):
    count=x.count(x[0])
    for i in range(count):
        x.remove(x[0])
    return(x)
def third_largest_number (x):
    x.sort(reverse=True)
    remove_largest(x)
    remove_largest(x)
    return(x[0])
    
A=[1,2,3,2,2,2,2,23,2,1,12,22,]

print(third_largest_number(A))