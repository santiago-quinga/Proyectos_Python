# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:59:48 2020

@author: Santiago Quinga
"""

dato=int(input("Ingrese un numero que queremos contar: "))
contador=1
acumulador=0
while True:
    print(contador)
    contador+=1
    if contador>dato:
        break
