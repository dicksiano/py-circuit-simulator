from src.editor.component import Component

# CONSTANTS
WIRE_WIDTH = 3
WIRE_COLOR = (150, 200, 200)

class Wire(Component):
    """Component that represent a logic gate"""

    def __init__(self, xStart, yStart, xEnd, yEnd, editor):
        Component.__init__(self, xStart, yStart, 0, 0, editor)

        # Start
        self.xStart = xStart
        self.yStart = yStart
        # First input
        self.xEnd = xEnd
        self.yEnd = yEnd

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
        screen.draw_line(WIRE_COLOR, self.xStart, self.yStart, self.xEnd, self.yEnd, WIRE_WIDTH)


class Wires(Component):
    """Component that holds all the gates"""

    def __init__(self, editor):
        self.editor = editor
        self.wires = []

        self.wire_start = []

    def add_wire(self, x, y):
        if len(self.wire_start) == 0:
            self.wire_start.append(x)
            self.wire_start.append(y)
        else:
            self.wires.append(Wire(self.wire_start[0], self.wire_start[1], x, y, self.editor))
            print("x = {0} y = {1} x = {2} y = {3}".format(self.wire_start[0], self.wire_start[1], x, y,))
            self.wire_start.clear()


    def update(self, mouse_pos):
        for wire in self.wires:
            wire.update(mouse_pos)

    def render(self, screen):
        for wire in self.wires:
            wire.render(screen)


