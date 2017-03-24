import pygame, sys, os
from pygame.locals import *

from src.editor.editor import Editor

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOUSE_BUTTON_LEFT = 1
MOUSE_BUTTON_RIGHT = 2
MOUSE_SCROLL_UP = 4
MOUSE_SCROLL_DOWN = 5

# INIT
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("Circuit Simulator")

# ASSETS
#IMAGE_PORT_NOT = pygame.image.load(os.path.join('res', 'port_not.png'))
#screen.blit(IMAGE_PORT_NOT, IMAGE_PORT_NOT.get_rect())

clock = pygame.time.Clock()
editor = Editor()

while True:
    # EVENT QUEUE
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            editor.on_mouse_move(event.pos[0], event.pos[1])
        elif event.type == MOUSEBUTTONUP:
            editor.on_mouse_click(event.pos[0], event.pos[1], event.button != MOUSE_BUTTON_LEFT)
        
    # UPDATE
    editor.update()

    # DRAW SCREEN
    screen.fill((255, 255, 255))
    editor.render(screen)
    pygame.display.flip()

    # FPS CAP
    clock.tick(60)