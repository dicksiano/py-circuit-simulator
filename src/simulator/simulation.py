
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
        if id == "in":
            self.gates_map[id] = { "type": type, "out": [] }
        elif id == "out":
            self.gates_map[id] = { "type": type, "in": None }
        elif id == "not":
            self.gates_map[id] = { "type": type, "in": None, "out": [] }
        else:
            self.gates_map[id] = { "type": type, "in1": None, "in2": None, "out": [] }

        if type == "in":
            self.input_pins.append(id)
        if type == "out":
            self.output_pins.append(id)

    def add_wire(self, from_gate_id, to_gate_id, to_gate_pin):
        if from_gate_id not in self.gates_map:
            return print("ERROR: Non-existent gate id '" + str(from_gate_id) + "'")
        if to_gate_id not in self.gates_map:
            return print("ERROR: Non-existent gate id '" + str(to_gate_id) + "'")
        if self.gates_map[from_gate_id]["type"] == "out":
            return print("ERROR: Gate of type 'out' can't have ouput wires")
        if self.gates_map[to_gate_id]["type"] == "in":
            return print("ERROR: Gate of type 'in' can't have input wires")
        if "in" in self.gates_map[to_gate_id] and not self.gates_map[to_gate_id]["in"] == None:
            return print("ERROR: Gates with fan in 1 can't have more than one input wire")
        if to_gate_pin == "in1" and not self.gates_map[to_gate_id]["in1"] == None:
            return print("ERROR: A gate can't have more than one wire in a single input pin")
        if to_gate_pin == "in2" and not self.gates_map[to_gate_id]["in2"] == None:
            return print("ERROR: A gate can't have more than one wire in a single input pin")    
        
        if self.gates_map[to_gate_id]["type"] == "not" or self.gates_map[to_gate_id]["type"] == "out":
            if not to_gate_pin == "in":
                return print("ERROR: Invalid gate pin '" + str(to_gate_pin) + "'")
            else:
                self.gates_map[to_gate_id][to_gate_pin] = from_gate_id
        else:
            if not to_gate_pin == "in1" and not to_gate_pin == "in2":
                return print("ERROR: Invalid gate pin '" + str(to_gate_pin) + "'")
            else:
                self.gates_map[to_gate_id][to_gate_pin] = from_gate_id

        self.gates_map[from_gate_id]["out"].append({ "id": to_gate_id, "pin": to_gate_pin })

    def run(self):
        input_state_list = []
        input_code_list = self._get_all_binary_numbers(len(self.input_pins))
        for code in input_code_list:
            input_state = {}
            for i, input_pin in enumerate(self.input_pins):
                input_state[input_pin] = code[i]
            input_state_list.append(input_state)

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

    def _get_all_binary_numbers(self, length):
        output = [ "" ]
        for i in range(length):
            new_output = []
            for number in output:
                new_output.append("0" + number)
            for number in output:
                new_output.append("1" + number)
            output = new_output
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
                    gate_states[gate["id"]] = { "out": "X" }
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
                output_gates = self.gates_map[gate["id"]]["out"]

                # propagate signal over wires
                for other_gate in output_gates:
                    if output_state == "X":
                        continue

                    if other_gate["pin"] in gate_states[other_gate["id"]]:
                        if gate_states[other_gate["id"]][other_gate["pin"]] == "X":
                            gate_states[other_gate["id"]][other_gate["pin"]] = output_state
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