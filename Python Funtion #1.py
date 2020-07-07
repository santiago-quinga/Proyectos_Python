# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:36:15 2020

@author: Santiago Quinga
"""

def isYearLeap(year):
#
     # Un año es bisiesto si cumple lo siguiente:
    # es divisible por 4 y no lo es por 100 ó si es divisible por 400.
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# En year podemos ingresar cualquier año 
# para poder realizar la prueba.
        
year=2020 # Ingrese un año que quiera.

print("¿El año %a es bisiesto?: %s" % (year, isYearLeap(year)))
print("\n"*0)
#
# Este es el codigo para verificar si el codigo funciona correctamente.      
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

