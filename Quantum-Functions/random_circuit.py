"""
This is a program which initializes a random path of quantum gates, and
then evaluates each gate in the path within it's specified parameters(Random
angle values, Random qubit values, etc).
"""

# Import statements(including qiskit methods)
import numpy as np
from random import choice, randrange
from qiskit import QuantumCircuit, Aer, execute

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


def random_circuit(depth, gatelist=[]):
    """
    Returns a randomized list of quantum gates based on
    a specified depth paramenter. This list represents
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

    # Base Case if the specified depth asks for no quantum fucntions
    if depth == 0:
        return gatelist

    # Intialize a variable that gives a random range based on the length of POTENTIAL_GATES
    gate_select = randrange(len(POTENTIAL_GATES))

    # Append a random gate to the initalized empty gatelist and recursively return the output
    gatelist.append(POTENTIAL_GATES[gate_select])
    return random_circuit(depth - 1, gatelist)


def evaluate_circuit(gatelist):
    """
    Returns a list of quantum gates with inputted random values for
    different qubits and angles, a circuit with each evaluated value,

    """
    qubit_input_list = []
    circuit = QuantumCircuit(2)
    theta = np.random.uniform(0, 2 * np.pi)
    lam = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    qubit_select = choice([0, 1])
    for gate in gatelist:
        if gate == ".x(":
            circuit.x(qubit_select)
            qubit_input_list.append(".x(" + str(qubit_select) + ")")
        elif gate == ".y(":
            circuit.y(qubit_select)
            qubit_input_list.append(".y(" + str(qubit_select) + ")")
        elif gate == ".z(":
            circuit.z(qubit_select)
            qubit_input_list.append(".z(" + str(qubit_select) + ")")
        elif gate == ".h(":
            circuit.h(qubit_select)
            qubit_input_list.append(".h(" + str(qubit_select) + ")")
        elif gate == ".sx(":
            circuit.sx(qubit_select)
            qubit_input_list.append(".sx(" + str(qubit_select) + ")")
        elif gate == ".sxdg(":
            circuit.sxdg(qubit_select)
            qubit_input_list.append(".sxdg(" + str(qubit_select) + ")")
        elif gate == ".t(":
            circuit.t(qubit_select)
            qubit_input_list.append(".t(" + str(qubit_select) + ")")
        elif gate == ".p(":
            circuit.p(theta, qubit_select)
            qubit_input_list.append(".p(" + str(theta) + ", " + str(qubit_select) + ")")
        elif gate == ".tdg(":
            circuit.tdg(qubit_select)
            qubit_input_list.append(".t(" + str(qubit_select) + ")")
        elif gate == ".cx(":
            if qubit_select == 0:
                circuit.cx(qubit_select, 1)
                qubit_input_list.append(".cx(0, 1)")
            else:
                circuit.cx(qubit_select, 0)
                qubit_input_list.append(".cx(1, 0)")
        elif gate == ".rxx(":
            if qubit_select == 0:
                circuit.rxx(theta, qubit_select, 1)
                qubit_input_list.append(".rxx(" + str(theta) + ", 0, 1)")
            else:
                circuit.rxx(theta, qubit_select, 0)
                qubit_input_list.append(".rxx(" + str(theta) + ", 1, 0)")
        elif gate == ".ryy(":
            if qubit_select == 0:
                circuit.ryy(theta, qubit_select, 1)
                qubit_input_list.append(".ryy(" + str(theta) + ", 0, 1)")
            else:
                circuit.ryy(theta, qubit_select, 0)
                qubit_input_list.append(".ryy(" + str(theta) + ", 0, 1)")
        elif gate == ".rzz(":
            if qubit_select == 0:
                circuit.rzz(theta, qubit_select, 1)
                qubit_input_list.append(".rzz(" + str(theta) + ", 0, 1)")
            else:
                circuit.rzz(theta, qubit_select, 0)
                qubit_input_list.append(".rzz(" + str(theta) + ", 0, 1)")
        elif gate == ".rx(":
            circuit.rx(theta, qubit_select)
            qubit_input_list.append(
                ".rx(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        elif gate == ".ry(":
            circuit.ry(theta, qubit_select)
            qubit_input_list.append(
                ".ry(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        elif gate == ".rz(":
            circuit.rz(theta, qubit_select)
            qubit_input_list.append(
                ".rz(" + str(theta) + ", " + str(qubit_select) + ")"
            )
        elif gate == ".s(":
            circuit.s(qubit_select)
            qubit_input_list.append(".s(" + str(qubit_select) + ")")
        elif gate == ".sdg(":
            circuit.sdg(qubit_select)
            qubit_input_list.append(".sdg(" + str(qubit_select) + ")")
        elif gate == ".swap(":
            if qubit_select == 0:
                circuit.swap(qubit_select, 1)
                qubit_input_list.append(".rz(" + str(qubit_select) + ",1)")
            else:
                circuit.swap(qubit_select, 0)
                qubit_input_list.append(".rz(" + str(qubit_select) + ",0)")
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
    circuit.measure_all()
    simulator = Aer.get_backend("qasm_simulator")
    result = execute(circuit, simulator, shots=1024).result()
    counts = result.get_counts(circuit)
    return qubit_input_list, circuit, counts


gatelist = random_circuit(3)
print(evaluate_circuit(gatelist))
