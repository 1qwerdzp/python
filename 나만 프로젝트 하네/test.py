import pygame
import sys
import random as r
from pygame.locals import *

pygame.init()
SC = pygame.display.set_mode((600, 600))
CL = pygame.time.Clock()
font=pygame.font.SysFont(None, 72)

img1=pygame.image.load('123a.png')
img2=pygame.image.load('123b.png')

l_s=img2.get_size()
m_s=img1.get_size()

m_x, m_y=250, 480

l_x=[]
l_y=[]

cnt=0

game_over=False

while True:
    if game_over :
        break
#B
    SC.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cnt += 1
    if cnt >= 20 :
        cnt = 0
        l_x.append(r.randint(0, 600))
        l_y.append(0)
    for i in range(len(l_x)) :
        l_y[i]+=5
        SC.blit(img2, (l_x[i], l_y[i]))
        if l_y==600:
            l_x=[]
            l_y=[]
        if l_y[i] >=550 :
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
        break

    key_e=pygame.key.get_pressed()
    if key_e[pygame.K_LEFT]:
        print(111111111)
        if m_x > 0:
            m_x -= 5
    if key_e[pygame.K_RIGHT]:
        if m_x < 500:
            m_x += 5

    SC.blit(img1, (m_x, m_y))

    for i in range(len(l_x)) :
        if l_x[i] + l_s[0] >= m_x and m_x + m_s[0] >= l_x[i] :
            if l_y[i] - l_s[1] >= m_y :
                msg =font.render("Game Over!", True, (255,0,0))
                SC.blit(msg, (160, 250))
                game_over = True
    pygame.display.update()
    CL.tick(60)

while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()