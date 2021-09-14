# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:21:24 2021

@author: Don
"""

import turtle 
t = turtle.Pen()
t.penup()
turtle.bgcolor('black')
sides = int(turtle.numinput('Number of sides','How many sides in your spiral of spirals? (2-6)',4,2,6))
colors =['red','yellow','green','orange','blue','purple']
for m in range(100):
    t.fd(m*4)
    pos = t.position()
    heading = t.heading()
    for n in range(int(m/2)):
        t.pd()
        t.pencolor(colors[n%sides])
        t.fd(2*n)
        t.rt(360/sides - 2)
        t.pu()
    t.setx(pos[0])
    t.sety(pos[1])
    t.setheading(heading)
    t.lt(360/sides + 2)