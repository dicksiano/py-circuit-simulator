import pygame, sys, os
from pygame.locals import *

from src.editor.editor import Editor

# CONSTANTS
SCREEN_SIZE = (800, 600)

# INIT
os.environ['SDL_VIDEO_CENTERED'] = '1'          # centers the window at startup
pygame.init()                                   # loads up pygame
pygame.font.init()                              # loads up the pygame font module
clock = pygame.time.Clock()                     # instantiates a pygame timer
surface = pygame.display.set_mode(SCREEN_SIZE)  # sets ups the screen size
pygame.display.set_caption("Circuit Simulator") # sets up the screen title

editor = Editor(surface)                        # instantiates the GUI

while True:
    # EVENT QUEUE
    for event in pygame.event.get(): # fowards events to event handling codepaths
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
    clock.tick(60)                   # caps at 60 updates and renders per second