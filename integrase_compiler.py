
import numpy as np

class Strand:
    #Initialize a circuit
    promoter = ['PROM']
    terminator = ['TERM']
    int_site = ['attB', 'attP']
    #Promoter, terminator, and integrase recognition sites.



def truth_table(user_input):
    # Build truth table based on user inputs.
    gates = []
    truth_table = np.zeros([2**user_input, 3])

    # Populate truth table with possible inputs
    truth_table[1,1] = 1
    truth_table[2,0] = 1
    truth_table[3,0] = 1
    truth_table[3,1] = 1

    truth_table[0,2] = user_input[0]
    truth_table[1,2] = user_input[1]
    truth_table[2,2] = user_input[2]
    truth_table[3,2] = user_input[3]

    for i in length(user_input):
        if truth_table[0,2] != "":
            gates.append('NOR')
            output.append(truth_table[0,2])
        if truth_table[3,2] != "":
            gates.append('AND')

    return truth_table

def determine_logic_gates(truth_table):

def flip(strand):
    # When two integrase sites are found in the proper configuration, flip the sequence between them.

def split(strand):
    # When two integrase sites are found in the proper configuration, excise the sequence between them.

def join(strand1, strand2):
    # Join two DNA strands together.

def evaluate(strand):
    # Evaluate whether the circuit matches its truth table.
