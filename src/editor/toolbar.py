import pygame, os

from src.editor.component import Component

class ToolbarButton(Component):
    """A clickable button of the toolbar"""

    def __init__(self, x, y, width, height, text):
        Component.__init__(self, x, y, width, height)

        self.text = text
        self.color = (200, 200, 200)
        self.click_count = 0

        # TODO change this to a singleton
        self.font = pygame.font.Font(os.path.join('res', 'open-sans.ttf'), 20)

    def on_mouse_click(self, x, y, button):
        self.click_count += 1
        self.text = "clicked! " + str(self.click_count)

    def on_mouse_enter(self):
        self.color = (220, 220, 220)

    def on_mouse_exit(self):
        self.color = (200, 200, 200)
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_bounds = text_surface.get_bounding_rect()
        text_x = self.x + (self.width - text_bounds.width) / 2 - text_bounds.x
        text_y = self.y + (self.height - text_bounds.height) / 2 - text_bounds.y
        screen.blit(text_surface, (text_x, text_y))

class Toolbar(Component):
    """Component that holds arrays of buttons for the UI"""

    def __init__(self):
        Component.__init__(self, 0, 0, 800, 50)

        self.buttons = []
        self.buttons.append(ToolbarButton(0, 0, 128, 50, "hue br"))
        self.buttons.append(ToolbarButton(128, 0, 128, 50, "hue br2"))
        
    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)
    
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
