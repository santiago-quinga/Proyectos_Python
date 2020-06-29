# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:11:21 2020

@author: Santiago Quinga
"""

dato=int(input("Ingrese un numero que queremos contar: "))
contador=1
acumulador=0
while True:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
    if contador>dato:
        break
print("\n"*1)
print("la suma de los",dato,"numeros es :",acumulador)
print("El promdeio total de los valores es:",acumulador//dato)

