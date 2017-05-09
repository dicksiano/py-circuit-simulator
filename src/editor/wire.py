from src.editor.component import Component

# CONSTANTS
WIRE_WIDTH = 3
WIRE_COLOR = (0, 0, 0)

class Wire:
    """Component that represents a wire in the screen"""

    def __init__(self, output, input):
        self.output = output
        self.input = input

    def render(self, screen):
        start_x = self.output.x + self.output.width/2
        start_y = self.output.y + self.output.height/2
        end_x = self.input.x + self.input.width/2
        end_y = self.input.y + self.input.height/2
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        screen.draw_line(WIRE_COLOR, start_x, start_y, mid_x, start_y, WIRE_WIDTH)
        screen.draw_line(WIRE_COLOR, mid_x, start_y, mid_x, end_y, WIRE_WIDTH)
        screen.draw_line(WIRE_COLOR, mid_x, end_y, end_x, end_y, WIRE_WIDTH)


class Wires(Component):
    """Component that holds all the wires"""

    def __init__(self, editor):
        self.editor = editor
        self.wires = []

        self.wire_start = []

    def add_wire(self, pin):
        if len(self.wire_start) == 0:  # First Pin
            self.wire_start.append(pin)
        else:  # Second Pin
            self.wires.append(Wire(self.wire_start[0], pin))
            self.wire_start[0].selected = False
            self.wire_start.clear()  # Clean

    def update(self, mouse_pos):
        pass

    def render(self, screen):
        for wire in self.wires:
            wire.render(screen)


