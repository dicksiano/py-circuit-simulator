from src.simulator.simulation import Simulation

simulation = Simulation()

# simulation.add_gate(gate_id, type)
simulation.add_gate("A", "in")
simulation.add_gate("B", "in")
simulation.add_gate("XNOR", "xnor2")
simulation.add_gate("NOT", "not")
simulation.add_gate("Y", "out")

# simulation.add_gate(from_gate_id, to_gate_id, to_gate_pin)
simulation.add_wire("A", "XNOR", "in1")
simulation.add_wire("B", "XNOR", "in2")
simulation.add_wire("XNOR", "NOT", "in")
simulation.add_wire("NOT", "Y", "in")

# simulation.run(input_state_list)
result = simulation.run()
print(result)
# [{'A': '0', 'B': '0', 'Y': '0'}, {'A': '1', 'B': '0', 'Y': '1'},
#    {'A': '0', 'B': '1', 'Y': '1'}, {'A': '1', 'B': '1', 'Y': '0'}]