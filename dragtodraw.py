# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:00:32 2021

@author: tohdo
"""

import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Drag to draw")
keep_going = True
YELLOW = (255,255,0)
radius = 15
mousedown = False
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, YELLOW, spot, radius)
    pygame.display.update()

pygame.quit()
        