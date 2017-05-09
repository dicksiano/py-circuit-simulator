
GATE_TYPE_LIST = [ "in", "out", "not", "and2", "nand2", "nor2", "or2", "xor2", "xnor2" ]

class Simulation:
    """Simulates the circuit logically"""

    def __init__(self):
        self.gates = []     # [{ id: int, type: string }]
        self.gates_map = {} # { id: { type: string, outputs:[], inputs:[] } }
        self.input_pins = []
        self.output_pins = []

    def add_gate(self, id, type):
        if type not in GATE_TYPE_LIST:
            return print("ERROR: Invalid gate type '" + str(type) + "'")
        if id in self.gates_map:
            return print("ERROR: Duplicated gate id '" + str(id) + "'")

        self.gates.append({ "id": id, "type": type })
        self.gates_map[id] = { "type": type, "outputs": [], "inputs": [] }

        if type == "in":
            self.input_pins.append(id)
        if type == "out":
            self.output_pins.append(id)

    def add_wire(self, from_gate_id, to_gate_id):
        if from_gate_id not in self.gates_map:
            return print("ERROR: Non-existent gate id '" + str(from_gate_id) + "'")
        if to_gate_id not in self.gates_map:
            return print("ERROR: Non-existent gate id '" + str(to_gate_id) + "'")
        if self.gates_map[from_gate_id]["type"] == "out":
            return print("ERROR: Gate of type 'out' can't have ouput wires")
        if self.gates_map[to_gate_id]["type"] == "in":
            return print("ERROR: Gate of type 'in' can't have input wires")
        if self.gates_map[to_gate_id]["type"] == "not" and len(self.gates_map[to_gate_id]["inputs"]) == 1:
            return print("ERROR: Gate of type 'not' can't have more than one input wire")
        if self.gates_map[to_gate_id]["type"] == "out" and len(self.gates_map[to_gate_id]["inputs"]) == 1:
            return print("ERROR: Gate of type 'out' can't have more than one input wire")
        if len(self.gates_map[to_gate_id]["inputs"]) == 2:
            return print("ERROR: Gate of type '" + self.gates_map[to_gate_id]["type"] \
                 + "' can't have more than two input wires")

        self.gates_map[to_gate_id]["inputs"].append(from_gate_id)
        self.gates_map[from_gate_id]["outputs"].append(to_gate_id)

    def run(self, input_state_list):
        output = []
        for input_state in input_state_list:
            end_state = {}
            output_state = self._simulate_for_input_states(input_state)
            for input_pin in input_state:
                end_state[input_pin] = input_state[input_pin]
            for output_pin in output_state:
                end_state[output_pin] = output_state[output_pin]
            output.append(end_state)
        return output
    
    def _simulate_for_input_states(self, input_states):
        # initial state of the simulation
        gate_states = {}
        undefined_states = 0
        for gate in self.gates:
            if gate["type"] == "in":
                if gate["id"] in input_states:
                    gate_states[gate["id"]] = { "out": input_states[gate["id"]] }
                else:
                    gate_states[gate["id"]] = "X"
            elif gate["type"] == "out":
                gate_states[gate["id"]] = { "in": "X" }
                undefined_states += 1
            elif gate["type"] == "not":
                gate_states[gate["id"]] = { "in": "X", "out": "X" }
                undefined_states += 2
            else:
                gate_states[gate["id"]] = { "in1": "X", "in2": "X", "out": "X" }
                undefined_states += 3
        last_undefined_states = undefined_states

        # simulation by iteration
        while True:
            for gate in self.gates:
                # skip gates without output since they can't affect the circuit
                if "out" not in gate_states[gate["id"]]:
                    continue

                output_state = gate_states[gate["id"]]["out"]
                output_gates = self.gates_map[gate["id"]]["outputs"]

                # propagate signal over wires
                for other_gate in output_gates:
                    if output_state == "X":
                        continue
                    if "in" in gate_states[other_gate]:
                        if gate_states[other_gate]["in"] == "X":
                            gate_states[other_gate]["in"] = gate_states[gate["id"]]["out"]
                            undefined_states -= 1
                    elif "in1" in gate_states[other_gate] or "in2" in gate_states[other_gate]:
                        if gate_states[other_gate]["in1"] == "X":
                            gate_states[other_gate]["in1"] = gate_states[gate["id"]]["out"]
                            undefined_states -= 1
                        elif gate_states[other_gate]["in2"] == "X":
                            gate_states[other_gate]["in2"] = gate_states[gate["id"]]["out"]
                            undefined_states -= 1
                
                # resolve gate logic if possible
                if output_state == "X":
                    if "in" in gate_states[gate["id"]]:
                        pin_in1 = gate_states[gate["id"]]["in"]
                        pin_in2 = "X"
                    elif "in1" in gate_states[gate["id"]] and "in2" in gate_states[gate["id"]]:
                        pin_in1 = gate_states[gate["id"]]["in1"]
                        pin_in2 = gate_states[gate["id"]]["in2"]
        
                    pin_out = self._get_logic_gate_output(gate["type"], pin_in1, pin_in2)
                    if not pin_out == "X":
                        gate_states[gate["id"]]["out"] = pin_out
                        undefined_states -= 1
                    
            # stop simuations if no changes occur in an iteration
            if last_undefined_states == undefined_states:
                break
            last_undefined_states = undefined_states

        # transcribe output pins states
        output_states = {}
        for output_pin in self.output_pins:
            output_states[output_pin] = gate_states[output_pin]["in"]
        return output_states

    def _get_logic_gate_output(self, type, pin_in1, pin_in2):
        pin_out = "X"

        if type == "not":
            if pin_in1 == "1":
                pin_out = "0"
            elif pin_in1 == "0":
                pin_out = "1"
        elif type == "and2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "1"
        elif type == "nand2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "0"
        elif type == "nor2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "0"
        elif type == "or2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "1"
        elif type == "xor2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "0"
        elif type == "xnor2":
            if pin_in1 == "0" and pin_in2 == "0":
                pin_out = "1"
            elif pin_in1 == "0" and pin_in2 == "1":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "0":
                pin_out = "0"
            elif pin_in1 == "1" and pin_in2 == "1":
                pin_out = "1"
        else:
            print("ERROR: Invalid port type '" + str(type) + "'")

        return pin_out