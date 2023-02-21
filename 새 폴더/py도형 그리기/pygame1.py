import sys
import pygame
from pygame.locals import *
pygame.init()
SU=pygame.display.set_mode((400,300))
pygame.display.set_caption("Tick Tock Timer")
C=pygame.time.Clock()
BL=(0,0,0)
W=(255,255,255)
R=(255,0,0)
G=(0,255,0)
B=(0,0,255)

while True:
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    SU.fill((255, 255, 255))
    re=Rect(20,10,60,40)

    pygame.draw.rect(SU,R,re)
    pygame.draw.circle(SU,G,(120,50),10)
    pygame.draw.polygon(SU,B, [[50,50], [0,100], [100,100]])
    pygame.draw.line(SU,BL, [120,0],[120,100])

    pygame.display.update()
    C.tick(1)