from src.simulator.simulation import Simulation

simulation = Simulation()

# simulation.add_gate(gate_id, type)
simulation.add_gate("A", "in")
simulation.add_gate("B", "in")
simulation.add_gate("AND", "xnor2")
simulation.add_gate("NOT", "not")
simulation.add_gate("Y", "out")

# simulation.add_gate(from_gate_id, to_gate_id)
simulation.add_wire("A", "AND")
simulation.add_wire("B", "AND")
simulation.add_wire("AND", "NOT")
simulation.add_wire("NOT", "Y")

# simulation.run(input_state_list)
result = simulation.run()
print(result)
# [{'A': '0', 'B': '0', 'Y': '0'}, {'A': '1', 'B': '0', 'Y': '1'},
#    {'A': '0', 'B': '1', 'Y': '1'}, {'A': '1', 'B': '1', 'Y': '0'}]