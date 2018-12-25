import sys, pygame
# Disable pylint for these lines
# Pygame extensions written in C are not properly handled by pylint
# pylint: disable=no-name-in-module
from pygame.constants import (QUIT)
# pylint: enable=no-name-in-module
# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()