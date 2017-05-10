from src.editor.mouse import Mouse
from src.editor.screen import Screen
from src.editor.toolbar import Toolbar
from src.editor.toolbar import MenuToolbar
from src.editor.gate import Gates
from src.editor.wire import Wires

from src.simulator.simulation import Simulation

class Editor:
    """GUI that interacts with the user to create and modify digital circuits"""
    
    # CONSTRUCTOR
    def __init__(self, surface):
        self.mouse = Mouse()
        self.screen = Screen(surface)
        self.toolbar = Toolbar(self)
        self.menutoolbar = MenuToolbar(self)
        self.gates = Gates(self)
        self.wires = Wires(self)

    # EVENT HANDLING
    def on_mouse_move(self, x, y):
        self.mouse.on_mouse_move(x, y)

    def on_mouse_down(self, x, y, button):
        self.mouse.on_mouse_down(x, y, button)
    
    def on_mouse_up(self, x, y, button):
        self.mouse.on_mouse_up(x, y, button)
    
    # GAME LOOP
    def update(self):
        self.toolbar.update(self.mouse)
        self.menutoolbar.update(self.mouse)
        self.gates.update(self.mouse)
        self.wires.update(self.mouse)

        self.mouse.update()

    def render(self):
        self.screen.draw_image("dot_pattern", (0, 66))
        self.toolbar.render(self.screen)
        self.menutoolbar.render(self.screen)
        self.wires.render(self.screen)
        self.gates.render(self.screen)

    def run_simulation(self):
        simulation = Simulation()
        gate_list = self.gates.get_list()
        wire_list = self.wires.get_list()
        for gate in gate_list:
            simulation.add_gate(gate["id"], gate["type"])
        for wire in wire_list:
            simulation.add_wire(wire["output"], wire["input"])
        result = simulation.run()

        print("SIMULATION")

        print("| ", end='')
        for gate in gate_list:
            if gate["type"] == 'in':
                print(gate["id"], end='')
                print(" | ", end='')
        for gate in gate_list:
            if gate["type"] == 'out':
                print(gate["id"], end='')
                print(" | ", end='')

        print()

        for line in result:
            for keys in line.keys():
                if keys[0] == 'I':
                    print("|  ", end='')
                    print(line[keys], end="  ")

            for keys in line.keys():
                if keys[0] == 'O':
                    print("|   ", end='')
                    print(line[keys], end="  ")
            print("|")

        print()
        print("TIMING DIAGRAM")

        for gate in gate_list:
            if gate["type"] == 'in' or gate["type"] == 'out':
                if gate["type"] == 'in':
                    print(gate["id"], end='')
                    print(":  ", end='')

                if gate["type"] == 'out':
                    print(gate["id"], end='')
                    print(": ", end='')

                for line in result:
                    for keys in line.keys():
                        if keys == gate["id"]:
                            if line[keys] == '0':
                                print("___", end='')
                            if line[keys] == '1':
                                print("---", end='')

                print()
