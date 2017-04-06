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

    def on_mouse_hold(self, x, y):
        self.x = x - self.width / 2
        self.y = y - self.height / 2

    def on_mouse_enter(self):
        pass

    def on_mouse_exit(self):
        pass

    def render(self, screen):
        screen.drawImage(self.image, (self.x, self.y))
        # Just for debug!
        # screen.fillRect((0, 255, 0), (self.connection_x, self.connection_y, 3, 3))
        #screen.fillRect((0, 255, 0), (self.second_input_x, self.second_input_y, 3, 3))
        # screen.fillRect((0, 255, 0), (self.connection_x, self.connection_y, 3, 3))


class Gates(Component):
    """Component that holds all the gates"""

    def __init__(self):

        self.gates = []
        self.gates.append(Gate(0, 100, GATE_WIDTH, GATE_HEIGHT, "port_and2"))
        #self.gates.append(Gate(50, 150, GATE_WIDTH, GATE_HEIGHT, "port_nand2"))
        #self.gates.append(Gate(50, 200, GATE_WIDTH, GATE_HEIGHT, "port_nor2"))
        #self.gates.append(Gate(50, 250, GATE_WIDTH, GATE_HEIGHT, "port_not"))
        #self.gates.append(Gate(50, 300, GATE_WIDTH, GATE_HEIGHT, "port_or2"))
        #self.gates.append(Gate(50, 350, GATE_WIDTH, GATE_HEIGHT, "port_xor2"))

    def update(self, mouse_pos):
        for gate in self.gates:
            gate.update(mouse_pos)

    def render(self, screen):
        for gate in self.gates:
            gate.render(screen)


