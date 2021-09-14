# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 06:10:04 2021

@author: Don
"""

import turtle
t =turtle.Pen()
number_of_circles = 6

for x in range(number_of_circles):
    t.circle(100)
    t.lt(360/number_of_circles)