# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:02:48 2020

@author: Santiago Quinga
"""


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()