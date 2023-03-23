"""
A program that randomizes which logic gates
quibits go into.
"""

from random import choice, randrange
from qiskit import IBMQ, QuantumCircuit, transpile


def firstinput(gate_one, _):
    """
    Return the first argument in a function
    """
    return gate_one


def secondinput(_, gate_two):
    """
    Return the second argument in a function
    """
    return gate_two


BASE_ARGUMENTS = [firstinput, secondinput]

POTENTIAL_GATES = {
    QuantumCircuit.h: 1,
    QuantumCircuit.y: 1,
    QuantumCircuit.x: 1,
    QuantumCircuit.z: 1,
    QuantumCircuit.p: 2,
    QuantumCircuit.s: 1,
    QuantumCircuit.t: 1,
}


def random_circuit(depth_min, depth_max):
    """
    Returns a randomly generated path of quantum gates that a quibit goes into
    based on previously defined functions from the "QuantumCircuit" file. These quantum gates
    are listed:

    Hadamard Gate: The H-Gate enables us to travel away from the Bloch sphere's
    poles and produce a superposition of 0 and 1. It basically transforms the state
    of a qubit between the x and z bases.
    X Gate: The x gate is a qubit rotation through pi radians around the x axis
    Y Gate: The y gate is a qubit rotation through pi radians around the y axis
    Z Gate: The z gate is a qubit rotation through pi radians around the z axis
    P Gate: The P-gate (phase gate) requires a number to tell it exactly what to perform
    because it is parametrized. The P-gate rotates degrees in the direction of the Z-axis.
    S Gate: The S gate is known as the phase gate or the Z90 gate, because it represents
    a 90-degree rotation around the z-axis.
    T Gate: S = T^2

    Args:
    depth_min: An int that represents the minimum amount of a gates a qubit should
    be passed through.
     depth_max: An int that represents the maximum amount of a gates a qubit should
    be passed through.

    Returns:



    """

    if depth_min < 1 or (depth_min < 1 and randrange(2) == 0):
        return choice(BASE_ARGUMENTS)

    gate = choice(list(POTENTIAL_GATES.keys()))
    first_gate = random_circuit(depth_min - 1, depth_max - 1)
    if POTENTIAL_GATES[gate] == 2:
        second_gate = random_circuit(depth_min - 1, depth_max - 1)

        def circuit(gate_one, gate_two):
            return gate(first_gate(gate_one, gate_two), second_gate(gate_one, gate_two))

    else:

        def circuit(gate_one, gate_two):
            return first_gate(gate_one, gate_two)

    return circuit
