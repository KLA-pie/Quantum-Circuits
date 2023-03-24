"""
A program that randomizes which logic gates
quibits go into.
"""

from random import choice, randrange, uniform
import numpy as np
from qiskit import IBMQ, QuantumCircuit, transpile

POTENTIAL_GATES = {
    1: QuantumCircuit.h,
    2: QuantumCircuit.y,
    3: QuantumCircuit.x,
    4: QuantumCircuit.z,
    5: QuantumCircuit.p,
    6: QuantumCircuit.s,
    7: QuantumCircuit.sdg,
    8: QuantumCircuit.t,
    9: QuantumCircuit.tdg,
    10: QuantumCircuit.cx,
    11: QuantumCircuit.swap,
    12: QuantumCircuit.sx,
    13: QuantumCircuit.sxdg,
    14: QuantumCircuit.rx,
    15: QuantumCircuit.ry,
    16: QuantumCircuit.rz,
    17: QuantumCircuit.rxx,
    18: QuantumCircuit.ryy,
    19: QuantumCircuit.rzz,
    20: QuantumCircuit.u,
}


def random_circuit(depth, gatelist):
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
    depth: An int that represents the amount of a gates a qubit should
    be passed through.


    Returns:

    """
    if depth == 0:
        return gatelist

    gate = list(POTENTIAL_GATES.keys())
    random_use = choice([0, 1])
    theta = np.random.uniform(0, 2 * np.pi)
    lam = np.random.uniform(0, 2 * np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    gate_select = randrange(len(POTENTIAL_GATES))
    qubit_select = choice([0, 1])

    gatelist.append(POTENTIAL_GATES[gate_select])
    return random_circuit(depth - 1, gatelist)


def evaluate_circuit(potential_gates)


eval("circuit.h(0)")
print(circuit)
