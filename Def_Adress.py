# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:37:38 2020

@author: Santiago Quinga
"""

def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("Su dirección es: ",calle,"sector : ",sector)
    print("Su casa es la #: ",numcasa,"Con codigo postal #: ",codigopostal)
    print("y esta cerca de: ",referencia)
    
print("Ingrese los datos que se solicitan de direccion ")   
c=input("Ingrese la calle: ")
s=input("Ingrese sector de residencia: ")
cod=input("Ingrese codigo postal: ")
r=input("Ingrese una referencia de su domicilio: ")
num=input("Ingrese el # de casa: ")

direccion(c,s,cod,r,num)