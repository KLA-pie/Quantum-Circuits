"""
Function to call and record jobs to IBM's backend
to run quantum simulations
"""
from qiskit import IBMQ, QuantumCircuit, transpile


def job_acquisition(gate_list):
    """
    Takes a given random quantum circuit and sends four requests to
    run qubits through IBM's backend and records the simulation IDs

    Args:
        gate_list: A list of ordered quantum gate instructions that a quantum circuit
        must follow. Each gate has different properties when activated

    Returns:
        The file `job_id_strings.txt` with each of the four new request IDs for every
        simulation ran with a given circuit configuration.
    """
    IBMQ.save_account(
        "471ff4b5279157f806c481c0e638ccb8f3a91fb834aea4c4b6397f7525a5e663d13bb0411d32a1517bffe273d6ca7fd2d98c22c8b61c176547e13a874eb52f53"
    )
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub="ibm-q", group="open", project="main")
    backend = provider.get_backend("ibmq_lima")
    quantum_circuit = QuantumCircuit(2)
    for gate in gate_list:
        eval("quantum_circuit" + gate)
    quantum_circuit.measure_all()
    with open("job_id_strings.txt", "w", encoding="utf8") as job_ids:
        for i in range(4):
            job = backend.run(transpile(quantum_circuit, backend=backend), shots=1024)
            job_ids.write(job.job_id())
            job_ids.write("\n")
    job_ids.close()
