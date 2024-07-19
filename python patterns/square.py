#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:17:14 2024

@author: SaiAnumala
"""
#n=int(input("enter a number:"))
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1  or j==0 or j==n-1:
            print("X ",end='')
        else:
            print(" ",end=' ')
    print()
    
   