"""
Function to call and record jobs to IBM's backend
to run quantum simulations
"""
from qiskit import IBMQ, execute, Aer


def job_acquisition(gate_list, quantum_circuit, iterations):
    """
    Takes a given random quantum circuit and sends four requests to
    run qubits through IBM's backend and records the simulation IDs

    Args:
        gate_list: A list of ordered quantum gate instructions that a quantum circuit
        must follow. Each gate has different properties when activated
        quantum_circuit: An object that details how the constructed circuit will function
        across the two qubits
        iterations: The number of times to run the circuit on IBM's backend

    Returns:
        The file `job_id_strings_(number).txt` with each of the four new request IDs for every
        simulation ran with a given circuit configuration where (number) is the depth of the
        circuit
    """
    # Load your IBM account onto your own compyter
    IBMQ.save_account("<Insert your unique API token>")
    IBMQ.load_account()

    # Acesss the backend to use the quantum computer
    backend = Aer.get_backend("qasm_simulator")

    # Write to a new file with a given qubit depth
    with open(
        "job_id_strings_" + str(len(gate_list)) + ".txt", "w", encoding="utf8"
    ) as job_ids:
        # Record the circuit that is being tested as well as its arguments
        job_ids.write(str(gate_list))
        job_ids.write("\n")
        # Execute and record the results for the number of iterations on the text file
        while iterations != 0:
            result = execute(quantum_circuit, backend, shots=1024).result()
            counts = result.get_counts(quantum_circuit)
            job_ids.write(str(counts))
            job_ids.write("\n")
            iterations -= 1
    job_ids.close()
