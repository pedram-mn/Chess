import pygame
from pygame.locals import *
import sys
screen = pygame.display.set_mode((900, 700))
ship = pygame.image.load("board.png")
screen.blit(ship, (0, 0))

shot = pygame.image.load("board.png")
shoot_y = 0


pygame.display.set_caption('galaxy invaders')

while True:
    x,y = pygame.mouse.get_pos()
    screen.blit(ship, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x

    if shoot_y > 0:
        screen.blit(shot, (shoot_x, shoot_y))
        shoot_y -= 10

    pygame.display.update()
    input("press")