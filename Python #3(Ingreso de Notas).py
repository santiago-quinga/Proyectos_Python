# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:07:06 2020

@author: Santiago Quinga
"""

#Entrada de datos.
Nota1=int(input("Ingrese su primera calificación: "))
Nota2=int(input("Ingrese su segunda calificación: "))
Nota3=int(input("Ingrese su tercera calificación: "))
#Imprimiremos para que nos de un salto.
print("\n " *0)
#Realizamos la operación
Total=Nota1+Nota2+Nota3
#Digitamos if como un condicinal que nos de 
#a selecionar si una variable ingresada es menor
#a 70.
if Nota1<70:
    #Realizamos otra operación si la Nota1 llega 
    #a ser menor que 70 esta suprime una resta.
    prome1=Total-Nota1
    #Imprimiremos el valor restado de la Nota1.
    print("Su calificación total es: ",prome1)
elif Nota2<70:
    #Realizamos otra operación si la Nota2 llega 
    #a ser menor que 70 esta suprime una resta.
    prome2=Total-Nota2
     #Imprimiremos el valor restado de la Nota2.
    print("Su calificación total es: ",prome2)    
elif Nota3<70:
    #Realizamos otra operación si la Nota3 llega 
    #a ser menor que 70 esta suprime una resta.
    prome3=Total-Nota3
     #Imprimiremos el valor restado de la Nota3.
    print("Su calificación total es: ",prome3)
else:
    #Imprimiremos el valor total de las notas si
    #estas no llegan hacer menor que 70.
    print("Su calificación total es: ",Total)
        