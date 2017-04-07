from src.editor.component import Component

# CONSTANTS
WIRE_WIDTH = 3
WIRE_COLOR = (200, 200, 200)

class Wire(Component):
    """Component that represent a logic gate"""

    def __init__(self, xStart, yStart, xEnd, yEnd):
        Component.__init__(self, xStart, yStart, 0, 0)

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
        screen.drawLine(WIRE_COLOR, self.xStart, self.yStart, self.xEnd, self.yEnd, WIRE_WIDTH)


class Wires(Component):
    """Component that holds all the gates"""

    def __init__(self):

        self.wires = []

    def add_wire(self):
        # TODO
        # Get Start and End of the wire
        # How do that with the mouse?

        self.wires.append(Wire(xStart, yStart, xEnd, yEnd))

    def update(self, mouse_pos):
        for wire in self.wiress:
            wire.update(mouse_pos)

    def render(self, screen):
        for wire in self.wires:
            wire.render(screen)


