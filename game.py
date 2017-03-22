import pygame, sys, os
from pygame.locals import *

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOUSE_BUTTON_LEFT = 1
MOUSE_BUTTON_RIGHT = 2
MOUSE_SCROLL_UP = 4
MOUSE_SCROLL_DOWN = 5

# INIT
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game")

# ASSETS
IMAGE_PORT_NOT = pygame.image.load(os.path.join('res', 'port_not.png'))

# APPLICATION
mouse_pos = (0, 0)
blocks = []
while True:

    # EVENT QUEUE
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_pos = event.pos
        elif event.type == MOUSEBUTTONUP and event.button == MOUSE_BUTTON_LEFT:
            blocks.append(event.pos)

    # DRAW SCREEN
    screen.fill((255, 255, 255))

    for block in blocks:
        pygame.draw.rect(screen, (0, 255, 0), (block[0] - 5, block[1] - 5, 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), (mouse_pos[0] - 5, mouse_pos[1] - 5, 10, 10))

    screen.blit(IMAGE_PORT_NOT, IMAGE_PORT_NOT.get_rect())

    pygame.display.flip()