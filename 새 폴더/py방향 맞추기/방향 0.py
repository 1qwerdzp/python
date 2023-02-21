import pygame, sys, random as r
from pygame.locals import *


pygame.init()
SC = pygame.display.set_mode((300, 300))
CL = pygame.time.Clock()

BL=(0,0,0)
W=(255,255,255)

fo=pygame.font.SysFont(None, 36)
tx=fo.render("",True,BL)

while True:
    SC.fill(W)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                tx=fo.render("UP",True,BL)
            if event.key==K_DOWN:
                tx=fo.render("DOWN",True,BL)
            if event.key==K_LEFT:
                tx=fo.render("LEFT",True,BL)
            if event.key==K_RIGHT:
                tx=fo.render("RIGHT",True,BL)
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    SC.blit(tx, (250,100))
    r
    pygame.display.update()
    CL.tick(60)