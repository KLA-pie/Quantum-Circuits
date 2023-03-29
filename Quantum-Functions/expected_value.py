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
    # Intialize a statevector with 00 as the only occurence as well as empty lists for the
    # final conjugate statevectors and final qubit probabilities
    statevector = np.array([1, 0, 0, 0])
    conjugate_statevector = []
    qubit_probabilities = []
    # Perform matrix multiplication on all respective gates in the circuit
    for i, gate in enumerate(gate_list):
        gate_composition = gate_matrix(gate)
        statevector = np.matmul(gate_composition, statevector)

    # Calculate the conjugate statevector and probabilties after the normal
    # statevector has been computed
    for i in range(4):
        conjugate_value = np.conjugate(statevector[i])
        conjugate_statevector.append(conjugate_value)
        qubit_probabilities.append(
            np.real(np.multiply(statevector[i], conjugate_statevector[i]))
        )

    # Return all values
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
    # Initialize identity matrix for Kronecker product
    iden_matrix = np.array([[1, 0], [0, 1]])

    # If the gate has at least one angle input, then generate a random
    # angle value
    if "," in gate and ".cx(" not in gate and ".swap(" not in gate:
        return angled_gate_matrix(gate)

    if ".x(" in gate or ".y(" in gate or ".z(" in gate or ".h(" in gate:
        transform_matrix = basic_gate_matrix(gate)

    # Matrix for swap gate (same reguardless of which qubits we are swtiching)
    if ".swap(" in gate:
        return np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    # Matricies for controlled NOT gate depdening on which qubit is the control
    if ".cx(" in gate:
        if "(0" in gate:
            return np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
        return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    # Matrix for S gate
    if ".s(" in gate:
        transform_matrix = np.array([[1, 0], [0, 1j]])
    # Matrix for S-Dagger gate
    if ".sdg(" in gate:
        transform_matrix = np.array([[1, 0], [0, -1j]])
    # Matrix for T gate
    if ".t(" in gate:
        transform_matrix = np.array([[1, 0], [0, 2**-0.5 + 1j * (2**-0.5)]])
    # Matrix for T-Dagger gate
    if ".tdg(" in gate:
        transform_matrix = np.array([[1, 0], [0, 2**-0.5 - 1j * (2**-0.5)]])
    # Matrix for SX gate
    if ".sx(" in gate:
        transform_matrix = np.array(
            [[0.5 + 0.5j, 0.5 - 0.5j], [0.5 - 0.5j, 0.5 + 0.5j]]
        )
    # Matrix for SX-Dagger gate
    if ".sxdg(" in gate:
        transform_matrix = np.array(
            [[0.5 - 0.5j, 0.5 + 0.5j], [0.5 + 0.5j, 0.5 - 0.5j]]
        )

    # Choose which qubit gets passed through the gate via the given input.
    if "0)" in gate:
        return np.kron(iden_matrix, transform_matrix)
    return np.kron(transform_matrix, iden_matrix)


def angled_gate_matrix(gate):
    """
    An extension of gate_matrix where it outputs and associates a given
    quantum gate to a respecitve 4 by 4 tranformation matrix to multiply
    the statevector by to get the new superposition states for gates that
    require phase angles

    Args:
        gate: A string that denotes the gate applied to a quantum circuit
        as well as which qubits the gate was applied to.

    Returns:
        A 4 by 4 transformation matrix with respect to the gate and the qubit
        input to update the statevector after passed through a quantum gate.
    """
    iden_matrix = np.array([[1, 0], [0, 1]])
    float_end = gate.find(",")
    theta = float(gate[gate.find("(") + 1 : float_end])
    # Matrix for RXX gate with a given angle input
    if ".rxx(" in gate:
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
    # Matrix for RYY gate with a given angle input
    if ".ryy(" in gate:
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
    # Matrix for RZZ gate with a given angle input
    if ".rzz(" in gate:
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
    # Matrix for phase gate of a given angle input
    if ".p(" in gate:
        phase_output = np.cos(theta) + np.sin(theta) * 1j
        transform_matrix = np.array([[1, 0], [0, phase_output]])
    # Matrix for RX gate
    if ".rx(" in gate:
        real_comp = np.cos(theta / 2)
        imag_comp = -1j * np.sin(theta / 2)
        transform_matrix = np.array([[real_comp, imag_comp], [imag_comp, real_comp]])
    # Matrix for RY gate
    if ".ry(" in gate:
        real_comp_cos = np.cos(theta / 2)
        real_comp_sin = np.sin(theta / 2)
        transform_matrix = np.array(
            [[real_comp_cos, -1 * real_comp_sin], [real_comp_sin, real_comp_cos]]
        )
    # Matrix for RZ gate
    if ".rz(" in gate:
        euler_identity = np.cos(theta / 2) + 1j * np.sin(theta / 2)
        euler_identity_conj = np.cos(theta / 2) + -1j * np.sin(theta / 2)
        transform_matrix = np.array([[euler_identity_conj, 0], [0, euler_identity]])
    # Matrix for U gate. Requires three phase angles to operate, so two other values are read
    if ".u(" in gate:
        gate = gate[float_end + 2 : :]
        float_end = gate.find(",")
        phi = float(gate[0:float_end])
        gate = gate[float_end + 2 : :]
        float_end = gate.find(",")
        lam = float(gate[0:float_end])
        transform_matrix = np.array(
            [
                [
                    np.cos(theta / 2),
                    -1 * (np.cos(lam) + 1j * np.sin(lam)) * np.sin(theta / 2),
                ],
                [
                    (np.cos(phi) + 1j * np.sin(phi)) * np.sin(theta / 2),
                    (np.cos(phi + lam) + 1j * np.sin(phi + lam)) * np.cos(theta / 2),
                ],
            ]
        )

    # Choose which qubit gets passed through the gate via the given input.
    if "0)" in gate:
        return np.kron(iden_matrix, transform_matrix)
    return np.kron(transform_matrix, iden_matrix)


def basic_gate_matrix(gate):
    """
    An extension of gate_matrix where it outputs and associates a given
    quantum gate to a respecitve 4 by 4 tranformation matrix to multiply
    the statevector by to get the new superposition states for gates that
    are Pauli gates or Hadamard gates

    Args:
        gate: A string that denotes the gate applied to a quantum circuit
        as well as which qubits the gate was applied to.

    Returns:
        A 2 by 2 transformation matrix with respect to be used in the Kronecker
        product for the 4 by 4 matrix
    """
    # Matrix for NOT gate (Also referred to as Pauli-X gate)
    if ".x(" in gate:
        return np.array([[0, 1], [1, 0]])
    # Matrix for Pauli-Y gate
    if ".y(" in gate:
        return np.array([[0, -1j], [1j, 0]])
    # Matrix for Pauli-Z gate
    if ".z(" in gate:
        return np.array([[1, 0], [0, -1]])
    # Matrix for Hadamard gate
    return np.array([[2**-0.5, 2**-0.5], [2**-0.5, -1 * 2**-0.5]])
