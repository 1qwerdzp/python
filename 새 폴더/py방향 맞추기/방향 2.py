import pygame, sys
from pygame.locals import *

pygame.init()
SC = pygame.display.set_mode((300, 300))
CL = pygame.time.Clock()

BL=(0,0,0)
W=(255,255,255)

fo=pygame.font.SysFont(None, 36)
tx=fo.render("",True,BL)

a=0

while True:
    SC.fill(W)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                a+=10
            if event.key==K_DOWN:
                a-=10
            if event.key==K_LEFT:
                a*=10
            if event.key==K_RIGHT:
                a/=10
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                a=0
    tx=fo.render('%d' %a,True,(0,0,0))
    SC.blit(tx, (100,120))
    pygame.display.update()
    CL.tick(60)