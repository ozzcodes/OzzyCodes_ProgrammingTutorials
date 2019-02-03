import pygame
from pygame.locals import *

pygame.init()

running = True

gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Test Game")
black = (0, 0, 0)
white = (255, 255, 255)
img = pygame.image.load("drone.jpeg")


def drone(x, y):
    gamewindow.blit(img, (x, y))


x = (800 * 0.45)
y = (600 * 0.7)

xChange = 0
yChange = 0
imageSpeed = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xChange = -5
        elif event.key == pygame.K_RIGHT:
            xChange = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            xChange = 0

    x += xChange
    y += yChange

    gamewindow.fill(white)
    drone(x, y)
    pygame.display.update()

var = pygame.QUIT
