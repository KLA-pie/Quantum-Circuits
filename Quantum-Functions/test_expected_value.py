"""
Check the correctness of the chi-squared calculator
"""

import numpy as np
import pytest

from expected_value import statevector_output

MATRIX_COMPARISON = [
    # Test the Hadamard gate on qubit 1
    (["test.h(0)"], [0.5, 0.5, 0, 0], [0.707106, 0.707106, 0, 0]),
    # Test the Hadamard gate on qubit 2
    (["test.h(1)"], [0.5, 0, 0.5, 0], [0.707106, 0, 0.707106, 0]),
    # Test the Pauli-X gate on qubit 1
    (["test.x(0)"], [0, 1, 0, 0], [0, 1, 0, 0]),
    # Test the Pauli-X gate on qubit 2
    (["test.x(1)"], [0, 0, 1, 0], [0, 0, 1, 0]),
    # Test the Pauli-Y gate on qubit 1
    (["test.y(0)"], [0, 1, 0, 0], [0, 1j, 0, 0]),
    # Test the Pauli-Y gate on qubit 2
    (["test.y(1)"], [0, 0, 1, 0], [0, 0, 1j, 0]),
    # Test the Pauli-Z gate on qubit 1
    (["test.z(0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the Pauli-Z gate on qubit 2
    (["test.z(1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the swap gate by swapping qubit 1 with qubit 2
    (["test.swap(0, 1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the swap gate by swapping qubit 2 with qubit 1
    (["test.swap(1, 0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the controlled not gate by using qubit 1 as the control
    # with qubit 1 being false
    (["test.cx(0, 1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the controlled not gate by using qubit 2 as the control
    # with qubit 2 being false
    (["test.cx(1, 0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the s gate on qubit 1 by rotating the qubit by π/2 radians
    # counterclockwise around the z axis
    (["test.s(0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the s gate on qubit 2 by rotating the qubit by π/2 radians
    # counterclockwise around the z axis
    (["test.s(1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the s-dagger gate on qubit 1 by rotating the qubit by π/2 radians
    # clockwise around the z axis
    (["test.sdg(0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the s-dagger gate on qubit 2 by rotating the qubit by π/2 radians
    # clockwise around the z axis
    (["test.sdg(1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the t-dagger gate on qubit 1 by rotating the qubit by π/4 radians
    # counterclockwise around the z axis
    (["test.t(0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the t-dagger gate on qubit 2 by rotating the qubit by π/4 radians
    # counterclockwise around the z axis
    (["test.t(1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the t-dagger gate on qubit 1 by rotating the qubit by π/4 radians
    # clockwise around the z axis
    (["test.tdg(0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the t-dagger gate on qubit 2 by rotating the qubit by π/4 radians
    # clockwise around the z axis
    (["test.tdg(1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the s gate on qubit 1 by rotating the qubit by π/2 radians
    # counterclockwise around the x axis
    (["test.sx(0)"], [0.5, 0.5, 0, 0], [0.5 + 0.5j, 0.5 - 0.5j, 0, 0]),
    # Test the s gate on qubit 2 by rotating the qubit by π/2 radians
    # counterclockwise around the x axis
    (["test.sx(1)"], [0.5, 0, 0.5, 0], [0.5 + 0.5j, 0, 0.5 - 0.5j, 0]),
    # Test the s-dagger gate on qubit 1 by rotating the qubit by π/2 radians
    # clockwise around the x axis
    (["test.sxdg(0)"], [0.5, 0.5, 0, 0], [0.5 - 0.5j, 0.5 + 0.5j, 0, 0]),
    # Test the s-dagger gate on qubit 2 by rotating the qubit by π/2 radians
    # clockwise around the x axis
    (["test.sxdg(1)"], [0.5, 0, 0.5, 0], [0.5 - 0.5j, 0, 0.5 + 0.5j, 0]),
    # Test the Phase gate by rotating qubit 1 π/2 radians counterclockwise
    # around the z axis
    (["test.p(1.57079632679, 0)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the Phase gate by rotating qubit 2 π/2 radians counterclockwise
    # around the z axis
    (["test.p(1.57079632679, 1)"], [1, 0, 0, 0], [1, 0, 0, 0]),
    # Test the Rotation-x gate by rotating qubit 1 π/2 radians counterclockwise
    # around the x axis
    (["test.rx(1.57079632679, 0)"], [0.5, 0.5, 0, 0], [0.707106, -0.707106j, 0, 0]),
    # Test the Rotation-x gate by rotating qubit 2 π/2 radians counterclockwise
    # around the x axis
    (["test.rx(1.57079632679, 1)"], [0.5, 0, 0.5, 0], [0.707106, 0, -0.707106j, 0]),
    # Test the Rotation-y gate by rotating qubit 1 π/2 radians counterclockwise
    # around the y axis
    (["test.ry(1.57079632679, 0)"], [0.5, 0.5, 0, 0], [0.707106, 0.707106, 0, 0]),
    # Test the Rotation-y gate by rotating qubit 2 π/2 radians counterclockwise
    # around the y axis
    (["test.ry(1.57079632679, 1)"], [0.5, 0, 0.5, 0], [0.707106, 0, 0.707106, 0]),
    # Test the Rotation-y gate by rotating qubit 1 π/2 radians counterclockwise
    # around the z axis
    (["test.rz(1.57079632679, 0)"], [1, 0, 0, 0], [0.707106 - 0.707106j, 0, 0, 0]),
    # Test the Rotation-y gate by rotating qubit 2 π/2 radians counterclockwise
    # around the z axis
    (["test.rz(1.57079632679, 1)"], [1, 0, 0, 0], [0.707106 - 0.707106j, 0, 0, 0]),
    # Test the rxx gate by entangling the two qubit probabilities and then
    # rotating qubit 1 π/2 radians counterclockwise around the x axis
    (["test.rxx(1.57079632679, 0)"], [0.5, 0, 0, 0.5], [0.707106, 0, 0, -0.707106j]),
    # Test the rxx gate by entangling the two qubit probabilities and then
    # rotating qubit 2 π/2 radians counterclockwise around the x axis
    (["test.rxx(1.57079632679, 1)"], [0.5, 0, 0, 0.5], [0.707106, 0, 0, -0.707106j]),
    # Test the ryy gate by entangling the two qubit probabilities and then
    # rotating qubit 1 π/2 radians counterclockwise around the y axis
    (["test.ryy(1.57079632679, 0)"], [0.5, 0, 0, 0.5], [0.707106, 0, 0, 0.707106j]),
    # Test the ryy gate by entangling the two qubit probabilities and then
    # rotating qubit 2 π/2 radians counterclockwise around the y axis
    (["test.ryy(1.57079632679, 1)"], [0.5, 0, 0, 0.5], [0.707106, 0, 0, 0.707106j]),
    # Test the rzz gate by entangling the two qubit probabilities and then
    # rotating qubit 1 π/2 radians counterclockwise around the z axis
    (["test.rzz(1.57079632679, 0)"], [1, 0, 0, 0], [0.707106 - 0.707106j, 0, 0, 0]),
    # Test the rzz gate by entangling the two qubit probabilities and then
    # rotating qubit 2 π/2 radians counterclockwise around the z axis
    (["test.rzz(1.57079632679, 1)"], [1, 0, 0, 0], [0.707106 - 0.707106j, 0, 0, 0]),
    # Test the U gate by rotating qubit 1 by 3 Euler angles each set to π/2
    (
        ["test.u(1.57079632679, 1.57079632679, 1.57079632679, 0)"],
        [0.5, 0.5, 0, 0],
        [0.707106, 0.707106j, 0, 0],
    ),
    # Test the U gate by rotating qubit 1 by 3 Euler angles each set to π/2
    (
        ["test.u(1.57079632679, 1.57079632679, 1.57079632679, 1)"],
        [0.5, 0, 0.5, 0],
        [0.707106, 0, 0.707106j, 0],
    ),
    # Test the U gate by using the respective Euler angles to get the Pauli-X gate
    (
        ["test.u(3.14159265359, 3.14159265359, 1.57079632679, 0)"],
        [0, 1, 0, 0],
        [0, -1, 0, 0],
    ),
    # Test the entanglement between two qubits using two Hadamard gates
    (["test.h(0)", "test.h(1)"], [0.25, 0.25, 0.25, 0.25], [0.5, 0.5, 0.5, 0.5]),
    # Test the entanglement between two qubits using two Hadamard gates with the
    # gates applied in reverse
    (["test.h(1)", "test.h(0)"], [0.25, 0.25, 0.25, 0.25], [0.5, 0.5, 0.5, 0.5]),
    # Test the controlled not gate by using qubit 1 as the control
    # with qubit 1 being true
    (["test.x(0)", "test.cx(0, 1)"], [0, 0, 0, 1], [0, 0, 0, 1]),
    # Test the controlled not gate by using qubit 2 as the control
    # with qubit 2 being true
    (["test.x(1)", "test.cx(1, 0)"], [0, 0, 0, 1], [0, 0, 0, 1]),
    # Test the controlled not gate by using qubit 1 as the control
    # with qubit 1 being true and with qubit 2 being true
    (["test.x(0)", "test.x(1)", "test.cx(0, 1)"], [0, 1, 0, 0], [0, 1, 0, 0]),
    # Test the controlled not gate by using qubit 2 as the control
    # with qubit 2 being true and with qubit 1 being true
    (["test.x(1)", "test.x(0)", "test.cx(1, 0)"], [0, 0, 1, 0], [0, 0, 1, 0]),
    # Test the swapping of two qubits when the polarities are opposite
    (["test.x(1)", "test.swap(0,1)"], [0, 1, 0, 0], [0, 1, 0, 0]),
    # Test rotating qubit 1 around the x axis π radians counterclockwise
    # and displace it by 13/45π radians counterclockwise around the
    # z axis for non standard angles
    (
        ["test.sx(0)", "test.p(0.90757121103, 0)"],
        [0.5, 0.5, 0, 0],
        [0.5 + 0.5j, 0.70183611 + 0.08617464j, 0, 0],
    ),
    # Test that the S and S-Dagger gates are complementary to eachother
    (
        ["test.sx(1)", "test.s(1)", "test.sdg(1)"],
        [0.5, 0, 0.5, 0],
        [0.5 + 0.5j, 0, 0.5 - 0.5j, 0],
    ),
    # Test that the T and T-Dagger gates are complementary to eachother
    (
        ["test.sx(1)", "test.t(1)", "test.tdg(1)"],
        [0.5, 0, 0.5, 0],
        [0.5 + 0.5j, 0, 0.5 - 0.5j, 0],
    ),
    # Test that the SX and SX-Dagger gates are complementary to eachother
    (
        ["test.sx(1)", "test.sxdg(1)"],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ),
    # Test that using rotations along the x axis of both qubits yields
    # equal probabilities of different superpositions
    (
        ["test.sx(0)", "test.sxdg(1)"],
        [0.25, 0.25, 0.25, 0.25],
        [0.5 + 0j, 0 - 0.5j, 0 + 0.5j, 0.5 + 0j],
    ),
    # Test that using two entanglement gates either output 00 or 11
    (
        [
            "test.rxx(1.57079632679, 0)",
            "test.rzz(1.57079632679, 0)",
        ],
        [0.5, 0, 0, 0.5],
        [0.5 - 0.5j, 0 + 0j, 0 + 0j, -0.5 - 0.5j],
    ),
    # Test that using all entanglement gates outputs a 00 with a phase angle
    (
        [
            "test.rxx(1.57079632679, 0)",
            "test.rzz(1.57079632679, 0)",
            "test.ryy(1.57079632679, 0)",
        ],
        [1, 0, 0, 0],
        [0.70710678 - 0.707106781j, 0, 0, 0],
    ),
]


@pytest.mark.parametrize("gate_list, probabilities, statevector", MATRIX_COMPARISON)
def test_statevector_output(gate_list, probabilities, statevector):
    """
    Test that an implementation for a selected qubit gate outputs the correct
    matrix to multiply the statevector by.

    Args:
        gate_list: The list of quantum gates two qubits will pass through before their states
        are measured
        probabilities: The list of probabilities the instances of 00, 01, 10, and 11 are expected
        to occur respecitvely
        statevector: The associated statevector that corresponds to the phase angle of a given qubit
        state which also gives information about the probability composition of a qubit instance
    """
    test_probabilities = statevector_output(gate_list)
    assert np.allclose(test_probabilities[0], probabilities)
    assert np.allclose(test_probabilities[1], statevector)
