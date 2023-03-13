# Quantum-Circuits
As classical computers face issues with computation, quantum computers have found its use in areas such as chemistry simulations and fast decryption. These quantum computers use qubits as opposed to normal bits in a classical computer which operate on a different basis through matrix representations in 3D space. However, due to the properties of quantum mechanics, sometimes the known state of these qubits are not always going to be exact after applying transformations to these qubits. Additionally, no quantum computer has implemented a form of accounting for these errors. This project analyzes how accurate these predicted states of 3 qubits compare to the measured state of 3 qubits when processed through a randomly generated quantum circuit arrangement.

## Required Software
To run the software, you will need the following:
* IBM Qiskit library
* (Optional to run your own simulations) IBM API token

### IBM Qiskit library installation
To install the Qiskit library, do the following:
* Ensure that you're running a version of Python that is 3.7 or above
* Open a terminal for a version of Linux installed on your machine
* Once it loads, run the following command
```
pip install qiskit
```
* Be patient and wait for library to finish installing

### IBM API token
If you would like to get access to the quantum computers used in this project to run your own simulations, please do the following:
* Go to [quantum-computing.ibm.com](https://quantum-computing.ibm.com)
* Create an IBMid account if you do not have one already and follow the steps to set up your account. If you do, log in to your account.
* Once you have your account, go to the homepage
* On the homepage, you will see a section that says `API token` with a copy icon next to the asterisks. Click on the icon.
* What you have is your own unique API token to retrieve your own job requests to the IBM quantum backend. DO NOT SHARE THIS TOKEN WITH ANYONE!!!
* If there is a section in the files that are listed with a comment mentioning an API token, you may paste your API token to get your own job requests

If you have any questions, please feel free to reach out to Kevin Lie-Atjam (klieatjam@olin.edu) or Mihir Vemuri (mvemuri@olin.edu)
