#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:24:44 2024

@author: SaiAnumala
"""
"""n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()"""
    
n=5
for i in range(n):
    for j in range(n-i+1):
        print(" ",end="")
    print("*")
    for k in range(i+1):
        if i==n-1:
            print("*")
    print()
        
