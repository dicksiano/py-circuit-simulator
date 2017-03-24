import pygame, sys, os
from pygame.locals import *

from src.editor.editor import Editor

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# INIT
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.font.init()
surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
pygame.display.set_caption("Circuit Simulator")

# ASSETS
#IMAGE_PORT_NOT = pygame.image.load(os.path.join('res', 'port_not.png'))
#screen.blit(IMAGE_PORT_NOT, IMAGE_PORT_NOT.get_rect())

clock = pygame.time.Clock()
editor = Editor(surface)

while True:
    # EVENT QUEUE
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            editor.on_mouse_move(event.pos[0], event.pos[1])
        elif event.type == MOUSEBUTTONDOWN:
            editor.on_mouse_down(event.pos[0], event.pos[1], event.button)
        elif event.type == MOUSEBUTTONUP:
            editor.on_mouse_up(event.pos[0], event.pos[1], event.button)
        
    # UPDATE
    editor.update()

    # DRAW SCREEN
    surface.fill((255, 255, 255))
    editor.render()
    pygame.display.flip()

    # FPS CAP
    clock.tick(60)