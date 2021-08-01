# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:56:36 2021

@author: Don
"""

import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going= True
GREEN = (0,255,0)
radius = 50
pic = pygame.image.load('C:\\Users\\Don\\Pictures\\deadlycry.png')
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle(screen, GREEN, (100,100), radius)
    pygame.display.update()
    
    
pygame.quit()
