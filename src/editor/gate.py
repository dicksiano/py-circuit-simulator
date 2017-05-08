from src.editor.component import Component

# CONSTANTS
GATE_WIDTH = 65
GATE_HEIGHT = 47
GRID_SIZE = 16 # change to 32 later

class Input(Component):
    """Component that represents a input of a logic gate"""

    def __init__(self, x, y, width, height, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.x = x
        self.y = y

    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_drag(self, x, y):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_exit(self):
        pass

    def render(self, screen):
        pass

class Output(Component):
    """Component that represents the output of a logic gate"""

    def __init__(self, x, y, width, height, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.x = x
        self.y = y

    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_drag(self, x, y):
        pass

    def on_mouse_enter(self):
        pass

    def on_mouse_exit(self):
        pass

    def render(self, screen):
        pass

class Gate(Component):
    """Component that represents a logic gate"""

    def __init__(self, x, y, width, height, image, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.image = image

        self.first_input = Input(x, y + height * (1/3), 0.5, 0.5, editor)
        self.second_input = Input(x, y + height * (2/3), 0.5, 0.5, editor)
        self.output = Input(x + width, y + height/2, 0.5, 0.5, editor)

    def update_in_out(self):  # Update I/O
        self.output.x = self.x + self.width
        self.output.y = self.y + self.height / 2
        self.first_input.x = self.x
        self.first_input.y = self.y + self.height * (1 / 3)
        self.second_input.x = self.x
        self.second_input.y = self.y + self.height * (2 / 3)

    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_drag(self, x, y):
        self.x = ((x // 16) * 16) #- self.width / 2 + 16
        self.y = max(43, ((y // 16) * 16 + 11)) # FIXME hardcoded toolbar height
        self.update_in_out()

    def on_mouse_enter(self):
        pass

    def on_mouse_exit(self):
        pass

    def render(self, screen):
        screen.draw_image(self.image, (self.x, self.y))

class Gates(Component):
    """Collection of all the gates"""

    def __init__(self, editor):
        self.editor = editor
        self.gates = []

    def add_gate(self, x, y, width, height, image):
        self.gates.append(Gate(x, y, width, height, image, self.editor))

    def update(self, mouse_pos):
        for gate in self.gates:
            gate.update(mouse_pos)

    def render(self, screen):
        for gate in reversed(self.gates): # reversed() so things that are
            gate.render(screen)           # dragged first are on the front
