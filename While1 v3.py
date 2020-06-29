# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:46:13 2020

@author: Santiago Quinga
"""

dato=int(input("Ingrese el numero de veces que contare: "))
contador=1
acumulador=0
while contador<=dato:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
    promedio= acumulador//dato
print("\n"*1)
print("la suma de los",dato,"numeros es :",acumulador)
print("El promdeio total de los valores es:",promedio)
