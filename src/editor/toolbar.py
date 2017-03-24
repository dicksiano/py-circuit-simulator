import pygame, os

from src.editor.component import Component

class ToolbarButton(Component):
    def __init__(self, x, y, text):
        Component.__init__(self, x, y, 128, 50)

        self.text = text
        self.color = (200, 200, 200)

        self.font = pygame.font.Font(os.path.join('res', 'open-sans.ttf'), 20)

    def on_mouse_enter(self):
        self.color = (220, 220, 220)

    def on_mouse_exit(self):
        self.color = (200, 200, 200)
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.get_bounds())
        
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_bounds = text_surface.get_bounding_rect()
        screen.blit(text_surface, (self.x + (self.width - text_bounds.width) / 2 ,
            self.y + (self.height - text_bounds.height) / 2 - text_bounds.y))

class Toolbar(Component):
    def __init__(self):
        Component.__init__(self, 0, 0, 800, 50)

        self.buttons = []
        self.buttons.append(ToolbarButton(0, 0, "hue br"))

    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)
    
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
