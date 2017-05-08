from src.editor.component import Component

# CONSTANTS
GATE_WIDTH = 65
GATE_HEIGHT = 47
GRID_SIZE = 16 # change to 32 later
DELTA = 10

IS_ON_MOUSE_COLOR = (0, 200, 0)
IS_SELECTED_COLOR = (0, 0, 200)


class Pin(Component):
    """Component that represents input or output of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        Component.__init__(self, x, y, width, height, editor)
        self.gate = gate

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

class Input(Pin):
    """Component that represents a input of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        Pin.__init__(self, x - DELTA, y, width, height, editor, gate)
        self.isOnMouse = False
        self.isSelected = False

    def on_mouse_move(self, x, y):
        if not self.isSelected:
            self.isOnMouse = True

    def on_mouse_click(self, x, y, button):
        if not len(self.editor.wires.wire_start) == 0:
            self.editor.wires.add_wire(self)

            self.isOnMouse = False
            self.isSelected = True

    def on_mouse_drag(self, x, y):
        self.isOnMouse = False

    def on_mouse_enter(self):
        self.isOnMouse = False

    def on_mouse_exit(self):
        self.isOnMouse = False

    def render(self, screen):
        if self.isOnMouse:
            screen.fill_rect(IS_ON_MOUSE_COLOR, (self.x, self.y, 10, 10))
        elif self.isSelected:
            screen.fill_rect(IS_SELECTED_COLOR, (self.x, self.y, 10, 10))

class Output(Pin):
    """Component that represents the output of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        Pin.__init__(self, x + DELTA, y, width, height, editor, gate)
        self.isOnMouse = False
        self.isSelected = False

    def on_mouse_move(self, x, y):
        if not self.isSelected:
            self.isOnMouse = True

    def on_mouse_click(self, x, y, button):
        self.isOnMouse = False
        self.isSelected = True

        if len(self.editor.wires.wire_start) == 0:
            self.editor.wires.add_wire(self)

    def on_mouse_drag(self, x, y):
        self.isOnMouse = False

    def on_mouse_enter(self):
        self.isOnMouse = False

    def on_mouse_exit(self):
        self.isOnMouse = False

    def render(self, screen):
        if self.isOnMouse:
            screen.fill_rect(IS_ON_MOUSE_COLOR, (self.x, self.y, 10, 10))
        elif self.isSelected:
            screen.fill_rect(IS_SELECTED_COLOR, (self.x, self.y, 10, 10))

class Gate(Component):
    """Component that represents a logic gate"""

    def __init__(self, x, y, width, height, image, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.image = image

        self.first_input = Input(x, y + height * (1/3), 10, 10, editor, self)
        self.second_input = Input(x, y + height * (2/3), 10, 10, editor, self)

        self.output = Output(x + width, y + height/2, 10, 10, editor, self)

    def update_in_out(self):  # Update I/O
        self.output.x = self.x + DELTA + self.width
        self.output.y = self.y + self.height / 2

        self.first_input.x = self.x - DELTA
        self.first_input.y = self.y + self.height * (1 / 3)

        self.second_input.x = self.x - DELTA
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
