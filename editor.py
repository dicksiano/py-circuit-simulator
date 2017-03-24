import pygame

class Editor:
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.blocks = []

    def on_mouse_move(self, x, y):
        self.mouse_pos = (x, y)

    def on_mouse_click(self, x, y, is_rmb):
        self.blocks.append((x, y))
    
    def update(self):
        for i, block in enumerate(self.blocks):
            self.blocks[i] = (block[0] + 1, block[1])

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.mouse_pos[0] - 5, self.mouse_pos[1] - 5, 10, 10))

        for block in self.blocks:
            pygame.draw.rect(screen, (0, 255, 0), (block[0] - 5, block[1] - 5, 10, 10))