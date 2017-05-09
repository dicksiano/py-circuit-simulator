from src.editor.component import Component
from src.editor.gate import Gates
from src.editor.wire import Wires

# Map from button to it's gates asset
Gate = {
    "IN": "port_in",
    "OUT": "port_out",
    "AND": "port_and2",
    "NAND": "port_nand2",
    "NOR": "port_nor2",
    "NOT": "port_not",
    "OR": "port_or2",
    "XOR": "port_xor2",
    "XNOR": "port_xnor2"
}

# CONSTANTS
TOOLBAR_HEIGHT = 50

class ToolbarButton(Component):
    """A clickable button of the toolbar"""

    def __init__(self, x, y, width, height, text, editor):
        Component.__init__(self, x, y, width, height, editor)

        self.text = text
        self.color = (200, 200, 200)

    def on_mouse_click(self, x, y, button):
        self.color = (50, 50, 50)
        if self.text in Gate:
            self.editor.gates.add_gate(100, 100, 64, 47, Gate[self.text])
        elif self.text == "Reset":
            self.editor.gates.gates = []
            self.editor.wires.wires = []


    def on_mouse_down(self, x, y, button):
        self.color = (50, 50, 50)

    def on_mouse_up(self, x, y, button):
        self.color = (220, 220, 220)

    def on_mouse_enter(self):
        self.color = (220, 220, 220)

    def on_mouse_exit(self):
        self.color = (200, 200, 200)
    
    def render(self, screen):
        bounds = (self.x, self.y, self.width, self.height)
        screen.fill_rect(self.color, bounds)
        screen.draw_text_centered(self.text, (0, 0, 0), bounds)


class Toolbar(Component):
    """Component that holds arrays of gate buttons for the UI"""

    def __init__(self, editor):
        Component.__init__(self, 0, 0, 800, 55, editor)

        self.buttons = []
        button_names = ["IN", "OUT", "OR", "AND", "NOT", "NOR", "NAND", "XOR", "XNOR"]
        button_width = 800 // len(button_names) + 1 # FIXME hardcoded screen width
        for i, name in enumerate(button_names):
            self.buttons.append(ToolbarButton(i * button_width, 55, button_width, TOOLBAR_HEIGHT, name, editor))

    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)
    
    def render(self, screen):
        for button in self.buttons:
            button.render(screen)

class MenuToolbar(Component):
    """"Component that holds array of menu buttons for the UI"""

    def __init__ (self, editor):
        Component.__init__(self, 0, 0, 800, 50, editor)

        self.buttons = []
        button_names = ["Editor", "Simulation", "Result", "Reset"]
        button_width = 120
        for i, name in enumerate(button_names):
            if name == "Reset":
                self.buttons.append(ToolbarButton(800 - button_width, 0, button_width, TOOLBAR_HEIGHT, name, editor))
            else:
                self.buttons.append(ToolbarButton(i * button_width, 0, button_width, TOOLBAR_HEIGHT, name, editor))

    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)