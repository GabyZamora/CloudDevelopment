# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:09:08 2021

@author: GABRIELA
"""

import turtle

col=('red','yellow','green','cyan','pink','white')

t=turtle.Turtle()

screen=turtle.Screen()
screen.bgcolor('black')
t.speed(25)

for i in range (150):
    
    t.color(col [i%6] )
    t.forward(i*1.5)
    t.left(59)
    t.width(3)