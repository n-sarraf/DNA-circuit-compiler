# Possible functions: cut, flip
# Possible placements: before or after promoter
# Evaluate circuit after each placement

# Start with random placement of integrase sites. Cycle through potential
# integrase activity for each site until a circuit is reached that executes
# the desired logic. Do this ten times simultaneously.


def build_circuit(truth_table):
