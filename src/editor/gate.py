from src.editor.component import Component

# CONSTANTS
GATE_WIDTH = 60
GATE_HEIGHT = 60

class Gate(Component):
    """Component that represent a logic gate"""

    def __init__(self, x, y, width, height, image):
        Component.__init__(self, x, y, width, height)
        self.image = image

        # Out
        self.out_x = x + width;
        self.out_y = y + height/2;
        # First input
        self.first_input_x = x;
        self.first_input_y = y + height * (1/3);
        # First input
        self.second_input_x = x;
        self.second_input_y = y + height * (2/3);

    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_drag(self, x, y):
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def on_mouse_enter(self):
        pass

    def on_mouse_exit(self):
        pass

    def render(self, screen):
        screen.draw_image(self.image, (self.x, self.y))

class Gates(Component):
    """Component that holds all the gates"""

    def __init__(self):

        self.gates = []

    def add_gate(self, x, y, width, height, image):
        self.gates.append(Gate(x, y, width, height, image))

    def update(self, mouse_pos):
        for gate in self.gates:
            gate.update(mouse_pos)

    def render(self, screen):
        for gate in reversed(self.gates): # reversed() so things dragged first
            gate.render(screen)           # are on the front


