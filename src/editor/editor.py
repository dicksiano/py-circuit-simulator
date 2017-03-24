import pygame

from src.editor.toolbar import Toolbar

class Editor:
    # CONSTRUCTOR
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.blocks = []
        self.toolbar = Toolbar()

    # EVENT HANDLING
    def on_mouse_move(self, x, y):
        self.mouse_pos = (x, y)

    def on_mouse_click(self, x, y, is_rmb):
        self.blocks.append((x, y))
    
    # GAME LOOP
    def update(self):
        self.toolbar.update(self.mouse_pos)

    def render(self, screen):

        for block in self.blocks:
            pygame.draw.rect(screen, (0, 255, 0), (block[0] - 5, block[1] - 5, 10, 10))

        self.toolbar.render(screen)

        pygame.draw.rect(screen, (255, 0, 0), (self.mouse_pos[0] - 5, self.mouse_pos[1] - 5, 10, 10))