"""
t
"""
import numpy as np


def statevector_output(gate_list):
    """
    t
    """
    statevector = np.array([1, 0, 0, 0])
    conjugate_statevector = []
    qubit_probabilities = []
    for i, gate in enumerate(gate_list):
        gate_composition = gate_matrix(gate)
        statevector = np.matmul(gate_composition, statevector)

    for i in range(4):
        conjugate_value = np.conjugate(statevector[i])
        conjugate_statevector.append(conjugate_value)

    for i in range(4):
        qubit_probabilities.append(
            np.multiply(statevector[i], conjugate_statevector[i])
        )

    return qubit_probabilities, statevector, conjugate_statevector


# Base gate return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def gate_matrix(gate):
    """
    t
    """
    if ".h(" in gate:
        if "0" in gate:
            return np.array(
                [
                    [2**-0.5, 2**-0.5, 0, 0],
                    [-1 * 2**-0.5, 2**-0.5, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                ]
            )
        else:
            return np.array(
                [
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 2**-0.5, 2**-0.5],
                    [0, 0, -1 * 2**-0.5, 2**-0.5],
                ]
            )
    elif ".x(" in gate:
        if "0" in gate:
            return np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        else:
            return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    elif ".y(" in gate:
        if "0" in gate:
            return np.array([[0, -1j, 0, 0], [1j, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        else:
            return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1j], [0, 0, 1j, 0]])
    elif ".z(" in gate:
        if "0" in gate:
            return np.array([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        else:
            return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
    elif ".p(" in gate:
        pass
    elif ".s(" in gate:
        pass
    elif ".sdg(" in gate:
        pass
    elif ".t(" in gate:
        pass
    elif ".tdg(" in gate:
        pass
    elif ".cx(" in gate:
        pass
    elif ".swap(" in gate:
        return np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    elif ".rz(" in gate:
        pass
    elif ".sx(" in gate:
        pass
    elif ".sxdg(" in gate:
        pass
    elif ".rx(" in gate:
        pass
    elif ".ry(" in gate:
        pass
    elif ".rxx(" in gate:
        pass
    elif ".rzz(" in gate:
        pass
    elif ".u(" in gate:
        pass
