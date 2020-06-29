# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:07:05 2020

@author: Santiago Quinga
"""

#Ingresamos los datos de entrada.
Horas=float(input("Horas trabajadas: "))
Tarifa=float(input("Tarifa por hora: "))
Des=float(input("Descuentos: "))
#Imprimiremos para que nos de un salto.
print("\n "*0)
#Realizamos la operación.
total=Horas*Tarifa
#Digitamos if como un condicinal que nos de 
#a selecionar la variable ingresada es mayor
#a 40.
if Horas>40:
    #Realizamos otra operación para la Bonificación
    #si la variable llega a ser mayor a 40
    Descu=Tarifa*0.5
    valor=Descu*(Horas-40)
    Pago=total+valor-Des
    #Imprimiremos el valor del descuento.
    print("Valor a pagar es de: $",Pago)
#Si la variable ingresada es menor que
#40 no aplica la Bonificación
else:
    #Realizamos otra operación si la variable 
    #llega a ser menor a 40.
    destotal=total-Des
    #Impreme el valor sin aplicar la Bonificación.
    print("No cumple con las horas maximas de trabajo el cual", 
          "no tiene permitido una bonificación en su pago normal.")
    print("\n "*0)
    print("Valor a pagar es de: $",destotal)

