# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:16:24 2020

@author: Santiago Quinga
"""

ipadd={"R1":"10.0.0.1","R2":"10.0.0.2","R3":"10.0.0.3","S1":"10.1.0.1","S2":"10.1.0.2"}
print(type(ipadd))

dict1={"usuario1":"1756167159","valor":3000,"edad":19,"soltero":True,"RATE en %":53.5}

print(ipadd["S2"])
ipadd["languaje"]="stranger"
print("S1" in ipadd)
print("usuario1" in dict1)
