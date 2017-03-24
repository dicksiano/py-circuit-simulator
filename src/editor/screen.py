import pygame, os

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
        self.surface.blit(text_surface, (x - text_bounds.x, y - text_bounds.y - text_bounds.height))

    def drawTextCentered(self, string, color, rect):
        (x, y, width, height) = rect
        text_surface = self.font.render(string, True, color)
        text_bounds = text_surface.get_bounding_rect()
        text_x = x + (width - text_bounds.width) / 2 - text_bounds.x
        text_y = y + (height - text_bounds.height) / 2 - text_bounds.y
        self.surface.blit(text_surface, (text_x, text_y))