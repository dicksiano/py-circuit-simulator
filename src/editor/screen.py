import pygame, os

from src.editor.assets import Assets

class Screen:
    """Sandbox to allow components to draw on the screen avoiding the pygame api"""

    def __init__(self, surface):
        self.surface = surface
        self.width = surface.get_width()
        self.height = surface.get_height()

        self.font = pygame.font.Font(os.path.join('res', 'open-sans.ttf'), 20)

    def fillRect(self, color, rect):
        pygame.draw.rect(self.surface, color, rect)

    def drawText(self, string, color, pos):
        (x, y) = pos
        text_surface = self.font.render(string, True, color)
        text_bounds = text_surface.get_bounding_rect()
        text_x = x - text_bounds.x
        text_y = y - text_bounds.y - text_bounds.height
        self.surface.blit(text_surface, (text_x, text_y))

    def drawTextCentered(self, string, color, rect):
        (x, y, width, height) = rect
        text_surface = self.font.render(string, True, color)
        text_bounds = text_surface.get_bounding_rect()
        text_x = x + (width - text_bounds.width) / 2 - text_bounds.x
        text_y = y + (height - text_bounds.height) / 2 - text_bounds.y
        self.surface.blit(text_surface, (text_x, text_y))

    def drawImage(self, image_name, pos):
        image = Assets[image_name]
        rect = image.get_rect()
        self.surface.blit(image, (rect.x + pos[0], rect.y + pos[1], rect.width, rect.height))
    
    def drawImageCentered(self, image_name, pos):
        image = Assets[image_name]
        rect = image.get_rect()
        self.surface.blit(image, (rect.x + pos[0] - rect.width/2, \
            rect.y + pos[1] - rect.height/2,rect.width, rect.height))