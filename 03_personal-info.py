# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:25:39 2020

@author: Santiago Quinga
"""

Nombre=input("Ingresa tu nombre: ")
Apellido=input("Ingresa tu Apellido: ")
Ubicacion=input("Ingresea tu Ubicacion: ")
Edad=input("Ingresa tu edad: ")
space=" "
print("\n " *1)
print("Hola que tal un gusto en conocerte"+space+Nombre+space+
      "y tu apellido paterno debe ser"+space+Apellido+space+
      "y me imagino que talvez eres de"+space+Ubicacion+space+
      "Verdad y tienes"+space+Edad+space+"años")
Edad=int(Edad) 
if Edad>= 1 and Edad<=5:
    print("eres un niño todavia.")
elif Edad>=6 and Edad<=9:
    print("eres un niño grande.")
elif Edad>=10 and Edad<=17:
    print("eres un adolescente.")
elif Edad>=18 and Edad<=39:
    print("eres un Adulto")
elif Edad>=40 and Edad<=80:
    print("eres un Adulto Mayor")
else: 
    print("tienes ya largo de vivir.")   