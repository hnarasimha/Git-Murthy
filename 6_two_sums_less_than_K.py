#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:15:28 2020

@author: mharesam

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.

"""

def two_sums_less_than_K (A,K):
        index_1 = 0
        index_2 = 0
        i = 0
        S=[]
        for i in range (len(A)):
            for j in range (1,len(A)):
                if (A[i]+A[j]) < K and i < j:
                    index_1,index_2=i,j
                    S.append(A[i]+A[j])

            
        if index_1 == 0 and index_2 == 0:
            return -1
        else:
            print (index_1)
            print (index_2)
            return (max(S))


A = [358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549]
K = 1800
print(two_sums_less_than_K (A,K))