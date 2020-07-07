# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:49:57 2020

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
# Definimos a daysInMonth para que nos pueda ayudar 
# Como un retorno de datos.
def daysInMonth(year, month):
    # Ingresamos la condicional if
    # Para poder evaluar que mes
    # Dispone de 28,29,30 y 31 dias.
    if isYearLeap(year) and month==2:
        return 29
    elif month==2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else: 
        return 31
#  En month ingresamos caulquier numero del mes.
        
month= 2 # Ingrese un numero del mes.

print("El total de dias del año",year,"del mes %i son: %s"
      % (month, daysInMonth(year, month)),"dias")
print("\n"*0)
#
# Este es el codigo para verificar si el codigo funciona correctamente. 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

