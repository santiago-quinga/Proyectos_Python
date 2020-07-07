# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:00:08 2020

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
#
# Definimos a daysInMonth para que nos pueda ayudar 
# Como un retorno de datos.
def daysInMonth(year, month):
    # Ingresamos la condicional if
    # Para poder evaluar que mes
    # Dispone de 28,29,30 y 31 dias.
    if isYearLeap(year) and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
#
def dayOfYear(year, month, day):
    numberOfDays = 0
    # Ciclo del mes 1 hasta month-1
    for i in range(1, month):
        numberOfDays = numberOfDays + daysInMonth(year, i)

    # Sumo los dias del mes actual
    numberOfDays = numberOfDays + day
    return numberOfDays

# Aqui podemos ingresar el año, mes y dia que queremos evaluar.
year = 2019
month = 3
day = 1

print("El total de dias trancuridos de la fecha (", year, "/", month, "/",
      day, ") son:", dayOfYear(year, month, day), "dias en total")
