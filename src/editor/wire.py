from src.editor.component import Component

# CONSTANTS
WIRE_WIDTH = 3
WIRE_COLOR = (150, 200, 200)

class Wire(Component):
    """Component that represent a logic gate"""

    def __init__(self, output, input, editor):
        Component.__init__(self, output.x, output.y, 0, 0, editor)
        self.output = output
        self.input = input

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
        screen.draw_line(WIRE_COLOR, self.output.x, self.output.y, self.input.x, self.input.y, WIRE_WIDTH)


class Wires(Component):
    """Component that holds all the gates"""

    def __init__(self, editor):
        self.editor = editor
        self.wires = []

        self.wire_start = []

    def add_wire(self, io):
        if len(self.wire_start) == 0:
            self.wire_start.append(io)
        else:
            self.wires.append(Wire(self.wire_start[0], io, self.editor))
            self.wire_start.clear()


    def update(self, mouse_pos):
        for wire in self.wires:
            wire.update(mouse_pos)

    def render(self, screen):
        for wire in self.wires:
            wire.render(screen)


