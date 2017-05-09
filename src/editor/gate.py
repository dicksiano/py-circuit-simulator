from src.editor.component import Component

# CONSTANTS
GATE_WIDTH = 65
GATE_HEIGHT = 47
GRID_SIZE = 16 # change to 32 later
PIN_RADIUS = 7
PIN_DIAMETER = 14

IS_ON_MOUSE_COLOR = (0, 200, 0)
IS_SELECTED_COLOR = (0, 0, 200)


class GatePin(Component):
    """Component that represents an input or output pin of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        Component.__init__(self, x - width/2, y - height/2, width, height, editor)
        self.gate = gate
        self.selected = False

    def render(self, screen):
        if self.mouse_hover or self.gate.mouse_hover:
            screen.draw_circle(IS_ON_MOUSE_COLOR, self.x + self.width/2, self.y + self.height/2, PIN_RADIUS, 4)
        elif self.selected:
            screen.draw_circle(IS_SELECTED_COLOR, self.x + self.width/2, self.y + self.height/2, PIN_RADIUS, 4)


class GateInputPin(GatePin):
    """Component that represents a input pin of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        GatePin.__init__(self, x, y, width, height, editor, gate)
        

    def on_mouse_click(self, x, y, button):
        if not len(self.editor.wires.wire_start) == 0:
            self.editor.wires.add_wire(self)


class GateOutputPin(GatePin):
    """Component that represents the output of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        GatePin.__init__(self, x, y, width, height, editor, gate)

    def on_mouse_click(self, x, y, button):
        self.selected = True

        if len(self.editor.wires.wire_start) == 0:
            self.editor.wires.add_wire(self)


class Gate(Component):
    """Component that represents a logic gate"""

    def __init__(self, x, y, width, height, image, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.image = image

        self.first_input = GateInputPin(x, y + height * (1 / 6.5), PIN_DIAMETER, PIN_DIAMETER, editor, self)
        self.second_input = GateInputPin(x, y + height * (1 - 1 / 6.5), PIN_DIAMETER, PIN_DIAMETER, editor, self)
        self.output = GateOutputPin(x + width, y + height/2, PIN_DIAMETER, PIN_DIAMETER, editor, self)

    def update_in_out(self):  # Update I/O
        self.output.x = self.x + self.width - self.output.width/2
        self.output.y = self.y + self.height / 2 - self.output.height/2

        self.first_input.x = self.x - self.output.width/2
        self.first_input.y = self.y + self.height * (1 / 6.5) - self.output.height/2

        self.second_input.x = self.x - self.output.width/2
        self.second_input.y = self.y + self.height * (1 - 1 / 6.5) - self.output.height/2

    def on_mouse_drag(self, x, y):
        self.x = ((x // 16) * 16) - 32 + 16 #- self.width / 2 + 16
        self.y = max(43, ((y // 16) * 16 + 11 - 32)) # FIXME hardcoded toolbar height
        self.update_in_out()

    def render(self, screen):
        screen.draw_image(self.image, (self.x, self.y))

        self.output.render(screen)
        self.first_input.render(screen)
        self.second_input.render(screen)

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
            gate.output.update(mouse_pos)
            gate.first_input.update(mouse_pos)
            gate.second_input.update(mouse_pos)

    def render(self, screen):
        for gate in reversed(self.gates): # reversed() so things that are
            gate.render(screen)           # dragged first are on the front
