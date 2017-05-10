from src.editor.mouse import Mouse
from src.editor.screen import Screen
from src.editor.toolbar import Toolbar
from src.editor.toolbar import MenuToolbar
from src.editor.gate import Gates
from src.editor.wire import Wires
from src.result.waveform import Waveform

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
        self.waveform = Waveform(self)

        self.active_screen = "Editor"

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
        self.menutoolbar.render(self.screen)
        if self.active_screen == "Editor":
            self.screen.draw_image("dot_pattern", (0, 66))
            self.toolbar.render(self.screen)
            self.wires.render(self.screen)
            self.gates.render(self.screen)
        elif self.active_screen == "Result":
            self.waveform.render(self.screen)

    def run_simulation(self):
        simulation = Simulation()
        gate_list = self.gates.get_list()
        wire_list = self.wires.get_list()
        for gate in gate_list:
            simulation.add_gate(gate["id"], gate["type"])
        for wire in wire_list:
            simulation.add_wire(wire["output"], wire["input"], wire["input_pin"])
        result = simulation.run()

        self.active_screen = "Result"
        self.waveform.is_result = True
        self.waveform.result = result
        self.waveform.gate_list = gate_list

        file = open("results/Simulation_Result.txt", "w")

        file.write("SIMULATION RESULTS\n")

        file.write("| ")
        for gate in gate_list:
            if gate["type"] == 'in':
                file.write(gate["id"])
                file.write(" | ")
        for gate in gate_list:
            if gate["type"] == 'out':
                file.write(gate["id"])
                file.write(" | ")

        file.write("\n")

        for line in result:
            for keys in line.keys():
                if keys[0] == 'I':
                    file.write("|  ")
                    file.write(line[keys])
                    file.write("  ")
            for keys in line.keys():
                if keys[0] == 'O':
                    file.write("|   ")
                    file.write(line[keys])
                    file.write("  ")
            file.write("|\n")

        file.write("\nTIMING DIAGRAM\n")

        for gate in gate_list:
            if gate["type"] == 'in':
                file.write(gate["id"])
                file.write(":  ")

                for line in result:
                    for keys in line.keys():
                        if keys == gate["id"]:
                            if line[keys] == '0':
                                file.write("___")
                            if line[keys] == '1':
                                file.write("---")

                file.write("\n")

        for gate in gate_list:
            if gate["type"] == 'out':
                file.write(gate["id"])
                file.write(": ")

                for line in result:
                    for keys in line.keys():
                        if keys == gate["id"]:
                            if line[keys] == '0':
                                file.write("___")
                            if line[keys] == '1':
                                file.write("---")

                file.write("\n")

        file.write("\n")
        file.close()
