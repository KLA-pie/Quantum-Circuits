"""
Functions that calculate the probability of all qubit configurations
after passing them through quantum gates and collapsing the superpositions
when measured.
"""
import numpy as np


def statevector_output(gate_list):
    """
    Calculates the statevector and qubit probabilitiy indicies after a
    quantum circuit has been executed in real time.

    Args:
        gate_list: A list of ordered quantum gate instructions that a quantum circuit
        must follow. Each gate has different properties when activated

    Returns:
        Outputs three 4 by 1 arrays of the following: A statevector with complex numbers
        as indicies of all qubit combinations, the statevector's respective complex
        conjugate statevector, and the probability density vector of all qubit combinations.
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


def gate_matrix(gate):
    """
    Outputs and associates a given quantum gate to a respecitve 4 by 4
    tranformation matrix to multiply the statevector by to get the new
    superposition states

    Args:
        gate: A string that denotes the gate applied to a quantum circuit
        as well as which qubits the gate was applied to.

    Returns:
        A 4 by 4 transformation matrix with respect to the gate and the qubit
        input to update the statevector after passed through a quantum gate.
    """
    iden_matrix = np.array([[1, 0], [0, 1]])
    if "," in gate and ".cx(" not in gate and ".swap(" not in gate:
        float_int = gate.find("(") + 1
        float_end = gate.find(",")
        theta = float(gate[float_int:float_end])

    if ".swap(" in gate:
        return np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    elif ".cx(" in gate:
        if "(0" in gate:
            return np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
        return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    elif ".rxx(" in gate:
        real_comp = np.cos(theta / 2)
        imag_comp = -1j * np.sin(theta / 2)
        return np.array(
            [
                [real_comp, 0, 0, imag_comp],
                [0, real_comp, imag_comp, 0],
                [0, imag_comp, real_comp, 0],
                [imag_comp, 0, 0, real_comp],
            ]
        )
    elif ".ryy(" in gate:
        real_comp = np.cos(theta / 2)
        imag_comp = -1j * np.sin(theta / 2)
        return np.array(
            [
                [real_comp, 0, 0, -1 * imag_comp],
                [0, real_comp, imag_comp, 0],
                [0, imag_comp, real_comp, 0],
                [-1 * imag_comp, 0, 0, real_comp],
            ]
        )
    elif ".rzz(" in gate:
        euler_identity = np.cos(theta / 2) + 1j * np.sin(theta / 2)
        euler_identity_conj = np.cos(theta / 2) + -1j * np.sin(theta / 2)
        return np.array(
            [
                [euler_identity_conj, 0, 0, 0],
                [0, euler_identity, 0, 0],
                [0, 0, euler_identity, 0],
                [0, 0, 0, euler_identity_conj],
            ]
        )
    elif ".h(" in gate:
        transform_matrix = np.array(
            [[2**-0.5, 2**-0.5], [2**-0.5, -1 * 2**-0.5]]
        )
    elif ".x(" in gate:
        transform_matrix = np.array([[0, 1], [1, 0]])
    elif ".y(" in gate:
        transform_matrix = np.array([[0, -1j], [1j, 0]])
    elif ".z(" in gate:
        transform_matrix = np.array([[1, 0], [0, -1]])
    elif ".p(" in gate:
        phase_output = np.cos(theta) + np.sin(theta) * 1j
        transform_matrix = np.array([[1, 0], [0, phase_output]])
    elif ".s(" in gate:
        transform_matrix = np.array([[1, 0], [0, 1j]])
    elif ".sdg(" in gate:
        transform_matrix = np.array([[1, 0], [0, -1j]])
    elif ".t(" in gate:
        transform_matrix = np.array([[1, 0], [0, 2**-0.5 + 1j * (2**-0.5)]])
    elif ".tdg(" in gate:
        transform_matrix = np.array([[1, 0], [0, 2**-0.5 - 1j * (2**-0.5)]])
    elif ".sx(" in gate:
        transform_matrix = np.array(
            [[0.5 + 0.5j, 0.5 - 0.5j], [0.5 - 0.5j, 0.5 + 0.5j]]
        )
    elif ".sxdg(" in gate:
        transform_matrix = np.array(
            [[0.5 - 0.5j, 0.5 + 0.5j], [0.5 + 0.5j, 0.5 - 0.5j]]
        )
    elif ".rx(" in gate:
        real_comp = np.cos(theta / 2)
        imag_comp = -1j * np.sin(theta / 2)
        transform_matrix = np.array([[real_comp, imag_comp], [imag_comp, real_comp]])
    elif ".ry(" in gate:
        real_comp_cos = np.cos(theta / 2)
        real_comp_sin = np.sin(theta / 2)
        transform_matrix = np.array(
            [[real_comp_cos, -1 * real_comp_sin], [real_comp_sin, real_comp_cos]]
        )
    elif ".rz(" in gate:
        euler_identity = np.cos(theta / 2) + 1j * np.sin(theta / 2)
        euler_identity_conj = np.cos(theta / 2) + -1j * np.sin(theta / 2)
        transform_matrix = np.array([[euler_identity_conj, 0], [0, euler_identity]])
    elif ".u(" in gate:
        gate = gate[float_end + 2 : :]
        float_end = gate.find(",")
        phi = float(gate[0:float_end])
        gate = gate[float_end + 2 : :]
        float_end = gate.find(",")
        lam = float(gate[0:float_end])
        entry_1 = np.cos(theta / 2)
        entry_2 = -1 * (np.cos(lam) + 1j * np.sin(lam)) * np.sin(theta / 2)
        entry_3 = (np.cos(phi) + 1j * np.sin(phi)) * np.sin(theta / 2)
        entry_4 = (np.cos(phi + lam) + 1j * np.sin(phi + lam)) * np.cos(theta / 2)
        transform_matrix = np.array([[entry_1, entry_2], [entry_3, entry_4]])

    if "0)" in gate:
        return np.kron(iden_matrix, transform_matrix)
    return np.kron(transform_matrix, iden_matrix)
