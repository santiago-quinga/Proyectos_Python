# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:33:49 2020

@author: Santiago Quinga
"""

result=0
n=5
for i in range(1, n + 1):
    print(i)
    result += i
    #print(result)
    #this ^^ is the shorthand for
    #result = result + i
    print("el resultado de la suma de 1 hasta n es:",
          result)