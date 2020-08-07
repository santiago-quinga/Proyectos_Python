# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:30:26 2020

@author: Santiago Quinga
"""

print('-- ANÁLISIS DE TEMPERATURA DEL AGUA --')
temp=[]
temp2=[]
cont=0
suma=0
suma2=0
n =int(input(" \nIngrese cantidad de temperaturas[1,10]: "))
while n<1 or n>10:
    print('\nEl valor debe ser entre 1 y 10')
    n=int(input('Ingrese cantidad de temperaturas [1,10]: '))
if n>=1 and n<=10:
    for i in range (1,n+1):
     print("\nTemperatura",i,"en C°:",end="")
     num= int(input())
     temp.append(num)
     cont+=1        
gas= 0
liq = 0
soli = 0
for k in range(0,n):
     if temp[k]>=100:
         gas+=1
     elif temp[k]>1 and temp[k]<100:
         liq+=1
     elif temp[k]<=0:
         soli+= 1
print("\nRESUMEN DEL ANÁLISIS DE MUESTRAS DE AGUA")
print("Cantidad de muestras sólidas:",soli)
print("Cantidad de muestras líquidas:",liq)
print("Cantidad de muestras gaseosas:",gas)
for i in range(0,n):
    suma+=temp[i]
prom=suma/cont
print('\nTemperatura Promedio °C:',prom)
for j in range(0,n):
        F=(temp[j]*9/5)+32
        temp2.append(F)
for k in range(0,n):
        suma2+=temp2[k]
prom2=suma2/cont
print('Temperatura Promedio °F:',prom2)