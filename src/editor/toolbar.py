from src.editor.component import Component
from src.editor.gate import Gates
from src.editor.wire import Wires
from src.result.waveform import Waveform

# Map from button to it's type
Gate = {
    "IN": "in",
    "OUT": "out",
    "AND": "and2",
    "NAND": "nand2",
    "NOR": "nor2",
    "NOT": "not",
    "OR": "or2",
    "XOR": "xor2",
    "XNOR": "xnor2"
}

# CONSTANTS
TOOLBAR_HEIGHT = 50

class ToolbarButton(Component):
    """A clickable button of the toolbar"""

    def __init__(self, x, y, width, height, text, editor,
                 default_color=(200, 200, 200), selection_color=(50, 50, 50), mouse_hover_color=(220, 220, 220)):
        Component.__init__(self, x, y, width, height, editor)

        self.text = text
        self.default_color = default_color
        self.selection_color = selection_color
        self.mouse_hover_color = mouse_hover_color

        self.color = self.default_color

    def on_mouse_click(self, x, y, button):
        self.color = self.selection_color
        if self.text in Gate:
            self.editor.gates.add_gate(100, 100, 64, 47, Gate[self.text])
        elif self.text == "Clear":
            self.editor.gates.gates = []
            self.editor.wires.wires = []
            self.editor.active_screen = "Editor"
            self.editor.waveform.is_result = False

        elif self.text == "Simulate":
            self.editor.run_simulation()
        elif self.text == "Editor":
            self.editor.active_screen = "Editor"
        elif self.text == "Result":
            if self.editor.waveform.is_result == True:
                self.editor.active_screen = "Result"


    def on_mouse_down(self, x, y, button):
        self.color = self.selection_color

    def on_mouse_up(self, x, y, button):
        self.color = self.mouse_hover_color

    def on_mouse_enter(self):
        self.color = self.mouse_hover_color

    def on_mouse_exit(self):
        self.color = self.default_color
    
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
        button_names = ["Editor", "Simulate", "Result", "Clear"]
        button_width = 120
        for i, name in enumerate(button_names):
            if name == "Clear":
                self.buttons.append(ToolbarButton(800 - button_width, 0, button_width, TOOLBAR_HEIGHT, name, editor,
                                                  (0, 200, 200), (0, 50, 50), (0, 220, 220)))
            else:
                self.buttons.append(ToolbarButton(i * button_width, 0, button_width, TOOLBAR_HEIGHT, name, editor,
                                                  (0, 200, 200), (0, 50, 50), (0, 220, 220)))

    def update(self, mouse_pos):
        for button in self.buttons:
            button.update(mouse_pos)

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)