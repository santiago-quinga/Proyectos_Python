# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:40:50 2020

@author: Santiago Quinga
"""

#Ingresamos los datos de entrada.
llantas=float(input("Cantidad de llantas a ingresar: "))
Precio=float(input("Precion unitario a ingresar: "))
#Imprimiremos para que nos de un salto.
print("\n " *0)
#Realizamos la operación.
Total = llantas*Precio
#Digitamos if como un condicinal que nos de 
#a selecionar si una variable ingresada es mayor
#o igual a 4.
if llantas>4:
    #Realizamos otra operación para el descuento
    #si la variable llega a ser mayor a 4
    descuento=Total*0.1
    destotal=Total-descuento
    #Imprimiremos el valor del descuento.
    print("Valor a pagar: $",destotal)
    #Si la variable ingresada es menor que
    #4 no aplica el decuento.
else:
    #Impreme el valor sin el descuento.
    print("Valor a pagar: $",Total)