# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:28:32 2021

@author: Don
"""

import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0,32)
pygame.display.set_caption('Collision Detection')
BLACK =(0,0,0)
RED = (255,0,0)
GREEN =(0,255,0)
WHITE =(255,255,255)

foodCounter=0
NEWFOOD=40
FOODSIZE=20
playerImg = pygame.image.load(r'C:\\Users\\Don\\Pictures\\deadlycry2.png').convert_alpha()
#rect = playerImg.get_rect()
#rect.center = (200, 300)
#windowSurface.blit(playerImg, [200,200])
#player =  windowSurface.blit(playerImg,(100,100))
#player = pygame.Rect(300, 100, 50, 50)
player= windowSurface.blit(playerImg,(100,100))
foods =[]
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key== K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key== K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key== K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key== K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key== K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key== K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key== K_UP or event.key == K_w:
                moveUp = False
            if event.key== K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWHEIGHT - player.width)
                
        if event.type ==MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
        foodCounter += 1
        if foodCounter >=NEWFOOD:
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH- FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
        windowSurface.fill(BLACK)
        
        if moveDown and player.bottom < WINDOWHEIGHT:
            player.top += MOVESPEED
        if moveUp and player.top > 0:
            player.top -= MOVESPEED
        if moveLeft and player.left>0:
            player.left -= MOVESPEED
        if moveRight and player.right < WINDOWWIDTH:
            player.right += MOVESPEED
        #windowSurface.blit(playerImg)
        pygame.draw.rect(windowSurface, RED, player)
        windowSurface.blit(playerImg,(player.x,player.y))
        #player()
        pygame.display.update()
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])
            
        pygame.display.update()
        mainClock.tick(40)
        