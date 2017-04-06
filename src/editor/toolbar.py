from src.editor.component import Component

# Map from button to it's gates asset
Gate = {
    "AND": "port_and2",
    "NAND": "port_nand2",
    "NOR": "port_nor2",
    "NOT": "port_not",
    "OR": "port_or2",
    "XOR": "port_xor2"
}

class ToolbarButton(Component):
    """A clickable button of the toolbar"""

    def __init__(self, x, y, width, height, text):
        Component.__init__(self, x, y, width, height)

        self.text = text
        self.color = (200, 200, 200)
        self.click_count = 0
        self.is_pressed = False

    def on_mouse_click(self, x, y, button):
        self.color = (50, 50, 50)
        # TODO
        # add new gates
        #append(Gate(100, 100, 60, 60, Gate[self.text]))

    def on_mouse_hold(self, x, y):
        self.color = (50, 50, 50)

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
        self.buttons.append(ToolbarButton(0, 0, 128, 50, "OR"))
        self.buttons.append(ToolbarButton(128, 0, 128, 50, "AND"))
        self.buttons.append(ToolbarButton(256, 0, 128, 50, "NOT"))
        self.buttons.append(ToolbarButton(384, 0, 128, 50, "NOR"))
        self.buttons.append(ToolbarButton(512, 0, 128, 50, "NAND"))
        self.buttons.append(ToolbarButton(640, 0, 128, 50, "XOR"))
        
    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)
    
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
