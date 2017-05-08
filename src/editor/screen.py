import pygame, os

from src.editor.assets import Assets

class Screen:
    """Sandbox to allow components to draw on the screen avoiding the pygame api"""

    def __init__(self, surface):
        self.surface = surface
        self.width = surface.get_width()
        self.height = surface.get_height()

        self.font = pygame.font.Font(os.path.join("res", "open-sans.ttf"), 20)

    def fill_rect(self, color, rect):
        pygame.draw.rect(self.surface, color, rect)

    def draw_text(self, string, color, pos):
        (x, y) = pos
        text_surface = self.font.render(string, True, color)
        text_bounds = text_surface.get_bounding_rect()
        text_x = x - text_bounds.x
        text_y = y - text_bounds.y - text_bounds.height
        self.surface.blit(text_surface, (text_x, text_y))

    def draw_text_centered(self, string, color, rect):
        (x, y, width, height) = rect
        text_surface = self.font.render(string, True, color)
        text_bounds = text_surface.get_bounding_rect()
        text_x = x + (width - text_bounds.width) / 2 - text_bounds.x
        text_y = y + (height - text_bounds.height) / 2 - text_bounds.y
        self.surface.blit(text_surface, (text_x, text_y))

    def draw_image(self, image_name, pos):
        image = Assets[image_name]
        rect = image.get_rect()
        self.surface.blit(image, (rect.x + pos[0], rect.y + pos[1], rect.width, rect.height))
    
    def draw_image_centered(self, image_name, pos):
        image = Assets[image_name]
        rect = image.get_rect()
        self.surface.blit(image, (rect.x + pos[0] - rect.width/2, \
            rect.y + pos[1] - rect.height/2,rect.width, rect.height))

    def draw_line(self, color, x_start, y_start, x_end, y_end, width):
        pygame.draw.line(self.surface, color, (x_start, y_start), (x_end, y_end), width)

    def draw_circle(self, color, x, y, radius, thickness):

        pygame.draw.circle(self.surface, color, (int(x), int(y)), radius, thickness)