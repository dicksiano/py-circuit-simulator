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
        self.connected = False

    def on_mouse_click(self, x, y, button):
        if self.connected:
            self.connected = False
            for wire in self.gate.editor.wires.wires:
                if wire.input == self:
                    self.gate.editor.wires.wires.remove(wire)
        else:
            if not len(self.editor.wires.wire_start) == 0:
                self.editor.wires.add_wire(self)
                self.connected = True


class GateOutputPin(GatePin):
    """Component that represents the output of a logic gate"""

    def __init__(self, x, y, width, height, editor, gate):
        GatePin.__init__(self, x, y, width, height, editor, gate)

    def on_mouse_click(self, x, y, button):
        if self.selected == False:
            self.selected = True

            if len(self.editor.wires.wire_start) == 0:
                self.editor.wires.add_wire(self)
        else:
            self.selected = False
            self.editor.wires.wire_start.clear()


class Gate(Component):
    """Component that represents a logic gate"""

    def __init__(self, x, y, width, height, type, editor):
        Component.__init__(self, x, y, width, height, editor)
        self.type = type

    def update_in_out(self):  # Update I/O
        pass

    def on_mouse_drag(self, x, y):
        self.x = ((x // 16) * 16) - 32 + 16 #- self.width / 2 + 16
        self.y = max(64 + 32 + 11, ((y // 16) * 16 + 11 - 32)) # FIXME hardcoded toolbar height
        self.update_in_out()

    def render(self, screen):
        pass

    def get_id(self):
        return str(self.editor.gates.index_of(self))

    def get_type(self):
        return self.type

class GateFanInOne(Gate):
    """Component that represents a logic gate with Fan In 1"""

    def __init__(self, x, y, width, height, type, editor, name=0):
        Gate.__init__(self, x, y, width, height, type, editor)

        if type == "in":
            self.name = "I" + str(name)
        if type == "out":
            self.name = "O" + str(name)

        if not type == "in":
            self.input = GateInputPin(x, y + height/2, PIN_DIAMETER, PIN_DIAMETER, editor, self)

        if not type == "out":
            self.output = GateOutputPin(x + width, y + height/2, PIN_DIAMETER, PIN_DIAMETER, editor, self)

    def update_in_out(self):  # Update I/O
        if not self.type == "out":
            self.output.x = self.x + self.width - self.output.width/2
            self.output.y = self.y + self.height / 2 - self.output.height/2

        if not self.type == "in":
            self.input.x = self.x - self.input.width/2
            self.input.y = self.y + self.height / 2 - self.input.height/2

    def render(self, screen):
        screen.draw_image(self.type, (self.x, self.y))

        if not self.type == "in":
            self.input.render(screen)
        if not self.type == "out":
            self.output.render(screen)

        if not self.type == "not":
            if self.mouse_hover:
                bounds = (self.x, self.y - self.height / 2, self.width, self.height)
                screen.draw_text_centered(self.name, (200, 0, 0), bounds)


class GateFanInTwo(Gate):
    """Component that represents a logic gate with Fan In 2"""

    def __init__(self, x, y, width, height, type, editor):
        Gate.__init__(self, x, y, width, height, type, editor)

        self.first_input = GateInputPin(x, y + height * (1 / 6.5), PIN_DIAMETER, PIN_DIAMETER, editor, self)
        self.second_input = GateInputPin(x, y + height * (1 - 1 / 6.5), PIN_DIAMETER, PIN_DIAMETER, editor, self)
        self.output = GateOutputPin(x + width, y + height/2, PIN_DIAMETER, PIN_DIAMETER, editor, self)

    def update_in_out(self):  # Update I/O
        self.output.x = self.x + self.width - self.output.width/2
        self.output.y = self.y + self.height / 2 - self.output.height/2

        self.first_input.x = self.x - self.first_input.width/2
        self.first_input.y = self.y + self.height * (1 / 6.5) - self.first_input.height/2

        self.second_input.x = self.x - self.second_input.width/2
        self.second_input.y = self.y + self.height * (1 - 1 / 6.5) - self.second_input.height/2

    def render(self, screen):
        screen.draw_image(self.type, (self.x, self.y))

        self.output.render(screen)
        self.first_input.render(screen)
        self.second_input.render(screen)


class Gates(Component):
    """Collection of all the gates"""

    def __init__(self, editor):
        self.editor = editor
        self.gates = []

        self.number_input = 0
        self.number_output = 0

    def add_gate(self, x, y, width, height, type):

        if len(self.gates) == 0:
            self.number_input = 0
            self.number_output = 0

        if type == "in" or type == "out" or type == "not":
            if type == "in":
                self.number_input = self.number_input + 1
                self.gates.append(GateFanInOne(x, y, width, height, type, self.editor, self.number_input))
            elif type == "out":
                self.number_output = self.number_output + 1
                self.gates.append(GateFanInOne(x, y, width, height, type, self.editor, self.number_output))
            else:
                self.gates.append(GateFanInOne(x, y, width, height, type, self.editor))
        else:
            self.gates.append(GateFanInTwo(x, y, width, height, type, self.editor))

    def update(self, mouse_pos):
        for gate in self.gates:
            gate.update(mouse_pos)

            if not (gate.type == "in" or gate.type == "out" or gate.type == "not"):
                gate.first_input.update(mouse_pos)
                gate.second_input.update(mouse_pos)
                gate.output.update(mouse_pos)
            else:
                if not gate.type == "out":
                    gate.output.update(mouse_pos)
                if not gate.type == "in":
                    gate.input.update(mouse_pos)

    def render(self, screen):
        for gate in reversed(self.gates): # reversed() so things that are
            gate.render(screen)           # dragged first are on the front

    def index_of(self, gate):
        if gate in self.gates:
            return self.gates.index(gate)
        else:
            return -1

    def get_list(self):
        result = []
        for i, gate in enumerate(self.gates):
            result.append({ "id": gate.get_id(), "type": gate.get_type() })
        return result