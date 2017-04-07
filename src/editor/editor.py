from src.editor.mouse import Mouse
from src.editor.screen import Screen
from src.editor.toolbar import Toolbar
from src.editor.assets import Assets

class Editor:
    """GUI that interacts with the user to create and modify digital circuits"""

    # CONSTRUCTOR
    def __init__(self, surface):
        self.mouse = Mouse()
        self.screen = Screen(surface)
        self.toolbar = Toolbar()

        self.blocks = []

    # EVENT HANDLING
    def on_mouse_move(self, x, y):
        self.mouse.on_mouse_move(x, y)

    def on_mouse_down(self, x, y, button):
        self.mouse.on_mouse_down(x, y, button)
    
    def on_mouse_up(self, x, y, button):
        self.mouse.on_mouse_up(x, y, button)
        self.blocks.append((x, y))
    
    # GAME LOOP
    def update(self):
        self.toolbar.update(self.mouse)
        for button in self.toolbar.buttons:
            button.gates.update(self.mouse)
        self.mouse.update()

    def render(self):
        image = Assets["dot_pattern"]
        rect = image.get_rect()
        self.screen.surface.blit(image, (0, 50, rect.width, rect.height))

        self.toolbar.render(self.screen)