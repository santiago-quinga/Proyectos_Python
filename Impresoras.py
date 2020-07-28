# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:28:04 2020

@author: Santiago Quinga
"""

inicial=int(input("Contador inicial: "))
final=int(input("Contador final: "))
total=final-inicial
if final<inicial:
    print("n\Error: El contador final es menor que el inicial",
          "Porfavor vuelva a ingresar el contador final")
    final=int(input("Contador final: "))
    otro=int(input("Impresora(1. B/N, 2. Color): "))
    total=final-inicial
    if otro==1:
        res=float(total*0.06)
    else:
        res=float(total*0.12)
else:
    otro=int(input("Impresora(1. B/N, 2. Color): "))
    if otro==1:
        res=float(total*0.06)
    else:
        res=float(total*0.12)
print("\nimpresiones:",total)
print("Costo: $",res)
        