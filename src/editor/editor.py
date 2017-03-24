from src.editor.mouse import Mouse
from src.editor.screen import Screen
from src.editor.toolbar import Toolbar

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
        self.mouse.update()

    def render(self):
        for block in self.blocks:
            self.screen.fillRect((0, 255, 0), (block[0] - 5, block[1] - 5, 10, 10))
        self.toolbar.render(self.screen)
        self.screen.fillRect((255, 0, 0), (self.mouse.x - 5, self.mouse.y - 5, 10, 10))