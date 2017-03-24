from src.editor.component import Component

class ToolbarButton(Component):
    """A clickable button of the toolbar"""

    def __init__(self, x, y, width, height, text):
        Component.__init__(self, x, y, width, height)

        self.text = text
        self.color = (200, 200, 200)
        self.click_count = 0

    def on_mouse_click(self, x, y, button):
        self.click_count += 1
        self.text = "clicked! " + str(self.click_count)

    def on_mouse_enter(self):
        self.color = (220, 220, 220)

    def on_mouse_exit(self):
        self.color = (200, 200, 200)
    
    def render(self, screen):
        bounds = (self.x, self.y, self.width, self.height)
        screen.fillRect(self.color, bounds)
        screen.drawTextCentered(self.text, (0, 0, 0), bounds)

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
