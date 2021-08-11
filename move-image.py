# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:36:22 2021

@author: Don
"""

import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])

pic = pygame.image.load('C:\\Users\\Don\\Pictures\\deadlycry2.png')
keep_going= True
GREEN = (0,255,0)
colorkey = pic.get_at((0,0))
BLACK = (0,0,0)
picx = 0
picy = 0
radius = 50
timer = pygame.time.Clock()
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += 1
    picy += 1
    screen.fill(BLACK)
    screen.blit(pic,(picx, picy))
    
    pygame.display.update()
    timer.tick(60)
    
pygame.quit()
