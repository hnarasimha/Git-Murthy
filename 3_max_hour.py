#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:04:42 2020

@author: mharesam
"""

def max_hour(A):
    hour=""
    print (hour)
    temp=[]
    temp = [i for i in A if i <= 2]
    if len(temp) == 0:
        return ""

    hour+=str(max(temp))
    print (hour)
    A.remove(max(temp))
    
    if max(temp) == 2:
        temp=[i for i in A if  i <= 3]
        if len(temp) == 0:
            return ""
        A.remove(max(temp))
        hour += str(max(temp))
    else:
        hour += str(max(A))
        A.remove(max(temp))
        
  
    hour+=":"
    print (hour)
    temp=[i for i in A if i <=5]
    if len(temp) == 0:
        return ""
    hour += str(max(temp))
    print (hour)
    A.remove(max(temp))
    hour += str(A[0])
    return(hour)

    
    
A=[2,0,0,6]
print(max_hour(A))
    
    