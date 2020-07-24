# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:18:24 2020

@author: Santiago Quinga
"""

import numpy as np
from random import randint
print("\nIngrese cuantas filas se requieren: ")
filas=int(input())    
print("\nIngrese cuantas columnas se requieren: ")
columnas=int(input())
print("\n"*0)
matrix=np.zeros([filas,columnas])
f=-1
c=-1
a=filas
b=filas
for i in range(0,filas):
    for n in range(0,columnas):
        matrix[i][n]=int(randint(0,99))
print("<< La matriz creada es de",filas,"x",columnas,">>")
print("\n"*0)
print(matrix)
print("\n"*0)
print('El valor de la diagonal principal de la matriz es: ')
print("\n"*0)
for j in range(0,filas):
    if f<filas:
        f+=1
        a-=1
    print(' | -- |'*f,"|",int(matrix[j][f]),"|",'| -- | '*a)
    
print('\nEl valor de la diagonal secundaria de la matriz es: ')
print("\n"*0)
for k in range(0,filas):
    if c<filas:
        c+=1
        b-=1
    print(' | -- |'*b,"|",int(matrix[k][b]),"|",'| -- | '*c)

