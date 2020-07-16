# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:18:16 2020

@author: Santiago Quinga
"""

import numpy as np
matrix=np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.int64)
print(matrix)
print("\n")
print("La matriz Tiene: ",matrix.ndim, " dimensiones")
print("\n")
print("El tipo de datos de la matriz es: ",matrix.dtype)
print("\n")
print("El tamaño de la matriz es:",matrix.size)
print("\n")
print("La forma de la matriz es:",matrix.shape)