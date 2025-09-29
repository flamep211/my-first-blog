'''
class Logger:
    def __init__(self, filename):
        self.filename = filename

        def write_log(self, message):
         with open(self.filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
            print(f"[LOG] Запписано сообщение: {message}")



class Dog:
    def __init__(self, name, logger):
        self.name = name
        self.logger = logger

    def bark(self):
        message = f"{self.name} лает!"
        print(message)
        self.logger.write_log(message)


logger = Logger ("dog_log.txt")
dog = Dog("Тоша", logger)

dog.bark()
dog.bark()
'''

import pygame
from pygame.examples.music_drop_fade import starting_pos

pygame.init()

dis=pygame.display.set_mode((1280, 960))
r = pygame.Rect(150, 100, 200, 200)

inner_rect = pygame.Rect(180, 130, 140, 140)
inner_color = (0,0,255)

Line_color = (255,0,0)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        if event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                pygame.quit()
    color=(255,255,0)
    pygame.draw.rect(dis, color, r, 0)
    pygame.draw.rect(dis, inner_color, inner_rect, 0)
    pygame.draw.line(dis, Line_color, (0,0), (200, 200), 2)

    pygame.display.update()
quit()