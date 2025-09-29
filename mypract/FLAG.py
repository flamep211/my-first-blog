import pygame
from pygame.colordict import THECOLORS

pygame.init()

dis = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Pygame Rectangles")
dis.fill(THECOLORS["darkgreen"])

rect_width = 50
rect_height = 50
padding = 10
font = pygame.font.SysFont(None, 24)

# Данные
with open("NUN.txt", "r") as f:
    filled_squares = set(int(line.strip()) for line in f if line.strip().isdigit())

y_pos = padding
count = 1

while y_pos + rect_height <= 1000:
    x_pos = padding
    while x_pos + rect_width <= 1000:

        if count in filled_squares:
            pygame.draw.rect(dis, (255, 0, 0), (x_pos, y_pos, rect_width, rect_height))  # Красный заполненый
        else:
            pygame.draw.rect(dis, (255, 255, 255), (x_pos, y_pos, rect_width, rect_height), 3)  # Белая рамка

        # Цифры внутри квадрата
        text = font.render(str(count), True, (255, 255, 255))
        text_rect = text.get_rect(center=(x_pos + rect_width // 2, y_pos + rect_height // 2))
        dis.blit(text, text_rect)

        count += 1
        x_pos += rect_width + padding
    y_pos += rect_height + padding

pygame.display.update()

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis_over = True

pygame.quit()
quit()
