# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:41:53 2020

@author: Santiago Quinga
"""

from random import randint
from time import sleep
temp = int()
lista=[int()for ind0 in range(100)]
tamaño=int(input("Ingrese el tamaño del vector: "))

for i in range(1,tamaño+1):
    lista[i-1]=randint(0,99)
    print("El valor en la posicion  ",i,"  es  ", lista[i-1]) 
    sleep(1)
sleep(1)
for j in range(1,tamaño+1):
    for l in range(1,tamaño):
        if lista[l-1]>lista[l]:
            temp = lista[l-1]
            lista[l-1]=lista[l]
            lista[l]=temp
for k in range(1,tamaño+1):
    print("El vector ordenado en la posicion  ",k,"  es ",lista[k-1]) 


