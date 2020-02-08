#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:09:41 2020

@author: mharesam
"""

def largestTimeFromDigits( A: List[int]) -> str:
		A.sort()
		if A[0] >= 3 or A[1]>=6:
			return ""
		for p in itertools.permutations(A[::-1]):
			if (p[0] * 10 + p[1]) < 24 and (p[2]*10 + p[3]) < 60:
				return str(p[0])+str(p[1])+":"+str(p[2])+str(p[3])
		return ""

    
A=[2,0,0,6]
print(largestTimeFromDigits(A))