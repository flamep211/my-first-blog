import time
from unittest.mock import right

import pygame
from pygame.colordict import THECOLORS

pygame.init()
dis=pygame.display.set_mode((600, 400))


dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(event)
            pygame.quit()
    dis.fill(THECOLORS["blue"])


    small = pygame.draw.circle(dis, (255, 255, 255), (300,100), 55)
    medium = pygame.draw.circle(dis, (255,255,255), (300, 200), 65)
    big = pygame.draw.circle(dis, (255,255,255), (300, 300), 75)


    brim = pygame.draw.rect(dis, (50, 50, 50), (240, 60, 120, 10))
    cylinder_body = pygame.draw.rect(dis, (80, 80, 80), (260, 20, 80, 45))
    pygame.draw.ellipse(dis, (80, 80, 80), (260, 15, 80, 15))

    scarf = pygame.draw.rect(dis, (255, 0, 0), (250, 135, 100, 20))
    scarf_down = pygame.draw.rect(dis, (200, 0, 0), (250, 155, 25, 60))


    right_eye = pygame.draw.circle(dis, (40, 40, 30), (285, 85), 6)
    left_eye = pygame.draw.circle(dis, (40, 40, 30), (325, 85), 6)


    right_arm = pygame.draw.line(dis, (137, 81, 41), (360, 200), (425, 300), 5 )
    left_arm = pygame.draw.line(dis, (137, 81, 41), (240, 200), (150, 300), 5)


    font = pygame.font.SysFont('Times New Roman', 20)
    y=0
    while y <250:
        y+=50
        text = font.render(('SNEGAYVIK'), True, THECOLORS['white'])
        dis.blit(text, (50, y))

    pygame.display.update()
    pygame.time.delay(1000)

quit()


'''
import time

import pygame
from pygame.colordict import THECOLORS

pygame.init()
dis=pygame.display.set_mode((600, 400))

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(event)
            pygame.quit()
    dis.fill(THECOLORS["green"])

    #Тело
    big = pygame.draw.circle(dis, (255, 255, 255), (300, 300), 75)
    medium = pygame.draw.circle(dis, (255, 255, 255), (300, 200), 65)
    small = pygame.draw.circle(dis, (255, 255, 255), (300, 100), 55)

    #Глаза и брови
    right_eye1 = pygame.draw.circle(dis, (200, 200, 200), (275, 85), 15)
    right_eye2 = pygame.draw.circle(dis, (40, 40, 40), (285, 85), 5)

    left_eye1 = pygame.draw.circle(dis, (200, 200, 200), (325, 85), 15)
    left_eye2 = pygame.draw.circle(dis, (40, 40, 40), (335, 85), 5)

    right_brow = pygame.draw.line(dis, (35, 35, 35), (265, 60), (300, 70), 7)
    left_brow = pygame.draw.line(dis, (35, 35, 35),(300, 70), (335, 60), 7)

    #Угольки
    coal1 = pygame.draw.circle(dis, (35, 35, 35), (300, 300), 10)
    coal2 = pygame.draw.circle(dis, (35, 35, 35), (300, 200), 10)
    coal3 = pygame.draw.circle(dis, (255, 128, 0), (300, 100), 10)

    #Шляпка

    #Фон
    font = pygame.font.SysFont('Times New Roman', 40)
    y=0
    while y <250:
        y+=50
        text = font.render(('I eat child'), True, THECOLORS['white'])
        dis.blit(text, (50, y))
        text = font.render(('I eat child'), True, THECOLORS['green'])
        dis.blit(text, (50, y-50))
    pygame.display.update()
    pygame.time.delay(1000)
quit()
'''





