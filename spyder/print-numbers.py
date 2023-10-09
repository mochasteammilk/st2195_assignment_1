#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:57:51 2023

@author: ziyan
"""

# Method 1
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Method 2a
for num in range(1,11):
    print(num, end=" ")
    
# Method 2b 
for i in range(1,11):
    print(i)
    
# Method 3
x=1
while(x<= 10):
    print(x)
    #x = x+1
    x+= 1