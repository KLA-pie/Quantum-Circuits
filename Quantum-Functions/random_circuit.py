"""
This is a program which initializes a random path of quantum gates, and
then evaluates each gate in the path within it's specified parameters(Random
angle values, Random qubit values, etc).
"""

# Import statements(including qiskit methods)
from random import choice, randrange
from qiskit import QuantumCircuit, Aer, execute
import numpy as np


# Define the potential gates as a dictionary
POTENTIAL_GATES = {
    0: ".u(",
    1: ".h(",
    2: ".y(",
    3: ".x(",
    4: ".z(",
    5: ".p(",
    6: ".s(",
    7: ".sdg(",
    8: ".t(",
    9: ".tdg(",
    10: ".cx(",
    11: ".swap(",
    12: ".sx(",
    13: ".sxdg(",
    14: ".rx(",
    15: ".ry(",
    16: ".rz(",
    17: ".rxx(",
    18: ".ryy(",
    19: ".rzz(",
}


def random_circuit(depth, gatelist):
    """
    Returns a randomized list of quantum gates based on
    a specified depth parameter. This list represents
    a path of gates that a randomized qubit is passed through,
    which then effectively changes it's superposition. This
    randomized path can be used for a random circuit vizualization.

    Args:
        depth: an int which specifies the amount of quantum gates that
        will be included in the final list.
        gatelist: an empty list(defined in the arguments) that is used in
        appending each of the randomized gates into it

    Returns:
        A list of strings(each mapped to a key in the global POTENTIAL_GATES
        dictionary) that represents randomized quantum gates and the path an
        inputted qubit would take.

    """

    # Base Case if the specified depth asks for no quantum functions
    if depth == 0:
        return gatelist

    # Intialize a variable that gives a random range based on the length of POTENTIAL_GATES
    gate_select = randrange(len(POTENTIAL_GATES))

    # Append a random gate to the initalized empty gatelist and recursively return the output
    gatelist.append(POTENTIAL_GATES[gate_select])
    return random_circuit(depth - 1, gatelist)


def evaluate_circuit(random_gatelist):
    """
    Returns a list of quantum gates with inputted random values for
    different qubits and angles, a circuit with these random gates and randomized inputs,
    and the qubit counts.

    Args:
        gatelist: An imputted list of quantum gates, this is meant to be the output of the
        random_circuit function, but any list of quantum gates in the specified format
        .<GATE>( will work in the following function.
    Returns:
        qubit_input_list: A list of strings of each random quantum gate, with randomly inputted
        values for each gate represented within parentheses of each gate.
        circuit: A qiskit object that represents the actual quantum circuit with the randomly
        inputted values.
        counts: A dictionary that maps each qubit instance (00,01,10,11) to the amount that
        each occurs in the random circuit.

    """
    # Defined list to append each logic gate to
    qubit_input_list = []
    # Initalize a qiskit object to add random value to
    circuit = QuantumCircuit(2)
    # Define random angle values and random qubit variables
    theta = np.random.uniform(0, 2 * np.pi)
    lam = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    qubit_select = choice([0, 1])
    # Iterate through each random gate in the inputted random Quantum gate list
    for gate in random_gatelist:
        # Input parameters for X gate and append to qubit_input_list
        if gate == ".x(":
            circuit.x(qubit_select)
            qubit_input_list.append(".x(" + str(qubit_select) + ")")
        # Input parameters for Y gate and append to qubit_input_list
        elif gate == ".y(":
            circuit.y(qubit_select)
            qubit_input_list.append(".y(" + str(qubit_select) + ")")
        # Input parameters for Z gate and append to qubit_input_list
        elif gate == ".z(":
            circuit.z(qubit_select)
            qubit_input_list.append(".z(" + str(qubit_select) + ")")
        # Input parameters for H gate and append to qubit_input_list
        elif gate == ".h(":
            circuit.h(qubit_select)
            qubit_input_list.append(".h(" + str(qubit_select) + ")")
        # Input parameters for SX gate and append to qubit_input_list
        elif gate == ".sx(":
            circuit.sx(qubit_select)
            qubit_input_list.append(".sx(" + str(qubit_select) + ")")
        # Input parameters for SXDG gate and append to qubit_input_list
        elif gate == ".sxdg(":
            circuit.sxdg(qubit_select)
            qubit_input_list.append(".sxdg(" + str(qubit_select) + ")")
        # Input parameters for T gate and append to qubit_input_list
        elif gate == ".t(":
            circuit.t(qubit_select)
            qubit_input_list.append(".t(" + str(qubit_select) + ")")
        # Input parameters for Pauli gate and append to qubit_input_list
        elif gate == ".p(":
            circuit.p(theta, qubit_select)
            qubit_input_list.append(".p(" + str(theta) + ", " + str(qubit_select) + ")")
        # Input parameters for TDG gate and append to qubit_input_list
        elif gate == ".tdg(":
            circuit.tdg(qubit_select)
            qubit_input_list.append(".t(" + str(qubit_select) + ")")
        # Input parameters for Controlled Not gate and append to qubit_input_list
        elif gate == ".cx(":
            if qubit_select == 0:
                circuit.cx(qubit_select, 1)
                qubit_input_list.append(".cx(0, 1)")
            else:
                circuit.cx(qubit_select, 0)
                qubit_input_list.append(".cx(1, 0)")
        # Input parameters for RXX gate and append to qubit_input_list
        elif gate == ".rxx(":
            if qubit_select == 0:
                circuit.rxx(theta, qubit_select, 1)
                qubit_input_list.append(".rxx(" + str(theta) + ", 0, 1)")
            else:
                circuit.rxx(theta, qubit_select, 0)
                qubit_input_list.append(".rxx(" + str(theta) + ", 1, 0)")
        # Input parameters for RYY gate and append to qubit_input_list
        elif gate == ".ryy(":
            if qubit_select == 0:
                circuit.ryy(theta, qubit_select, 1)
                qubit_input_list.append(".ryy(" + str(theta) + ", 0, 1)")
            else:
                circuit.ryy(theta, qubit_select, 0)
                qubit_input_list.append(".ryy(" + str(theta) + ", 0, 1)")
        # Input parameters for RZZ gate and append to qubit_input_list
        elif gate == ".rzz(":
            if qubit_select == 0:
                circuit.rzz(theta, qubit_select, 1)
                qubit_input_list.append(".rzz(" + str(theta) + ", 0, 1)")
            else:
                circuit.rzz(theta, qubit_select, 0)
                qubit_input_list.append(".rzz(" + str(theta) + ", 0, 1)")
        # Input parameters for RX gate and append to qubit_input_list
        elif gate == ".rx(":
            circuit.rx(theta, qubit_select)
            qubit_input_list.append(
                ".rx(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        # Input parameters for RY gate and append to qubit_input_list
        elif gate == ".ry(":
            circuit.ry(theta, qubit_select)
            qubit_input_list.append(
                ".ry(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        # Input parameters for RZ gate and append to qubit_input_list
        elif gate == ".rz(":
            circuit.rz(theta, qubit_select)
            qubit_input_list.append(
                ".rz(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        # Input parameters for S gate and append to qubit_input_list
        elif gate == ".s(":
            circuit.s(qubit_select)
            qubit_input_list.append(".s(" + str(qubit_select) + ")")
        # Input parameters for SDG gate and append to qubit_input_list
        elif gate == ".sdg(":
            circuit.sdg(qubit_select)
            qubit_input_list.append(".sdg(" + str(qubit_select) + ")")
        # Input parameters for SWAP gate and append to qubit_input_list
        elif gate == ".swap(":
            if qubit_select == 0:
                circuit.swap(qubit_select, 1)
                qubit_input_list.append(".rz(" + str(qubit_select) + ",1)")
            else:
                circuit.swap(qubit_select, 0)
                qubit_input_list.append(".rz(" + str(qubit_select) + ",0)")
        # Input parameters for U gate and append to qubit_input_list
        elif gate == ".u(":
            circuit.u(theta, phi, lam, qubit_select)
            qubit_input_list.append(
                ".u("
                + str(theta)
                + ", "
                + str(phi)
                + ", "
                + str(lam)
                + ", "
                + str(qubit_select)
                + ")"
            )
    # Simulate random circuit
    circuit.measure_all()
    simulator = Aer.get_backend("qasm_simulator")
    result = execute(circuit, simulator, shots=1024).result()
    counts = result.get_counts(circuit)
    # Return qubit_input_list, random qiskit circuit object, and counts
    return qubit_input_list, circuit, counts
