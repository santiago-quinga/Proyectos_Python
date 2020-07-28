# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:11:40 2020

@author: Santiago Quinga
"""

while True:
    x=input("Enter a number to count to: ")
    if x == "q" or x == "quit":
        break
else:
    x=int(x)
    y=1
while True:
    print(x)
    y=y+1
    if y>=x:
       break
    
