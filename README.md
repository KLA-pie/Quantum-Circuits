# Quantum-Circuits
As classical computers face issues with computation, quantum computers have found its use in areas such as chemistry simulations and fast decryption. These quantum computers use qubits as opposed to normal bits in a classical computer which operate on a different basis through matrix representations in 3D space. However, due to the properties of quantum mechanics, sometimes the known state of these qubits are not always going to be exact after applying transformations to these qubits. Additionally, no quantum computer has implemented a form of accounting for these errors. This project analyzes how accurate these predicted states of 2 qubits compare to the measured state of 2 qubits when processed through a randomly generated quantum circuit arrangement.

## Required Software
To run the software, you will need the following:
* IBM Qiskit library
* matplotlib
* numpy
* pylatexenc
* ipywidgets
* ipykernel
* (Optional to run your own simulations) IBM API token

### Library installation
To install the all of the necessary libraries, we recommend doing the following:
* Ensure that you're running a version of Python that is 3.7 or above
* Open a terminal for a version of Linux installed on your machine
* Once it loads, we recommend creating a new Anaconda environment. This can be done by doing the following
```
conda create --name <Environment Name> python=3.9
```
Where you may name your environment whatever you would like
* Be patient and make sure that you type y to create your environment after a dialog box appears
* After the environment has been created, run the following command
```
conda activate <Environment Name>
```
To activate your Anaconda environment
* You're now ready to install the libraries to use this repository. Ensure that your file directory is at the root of this repository. By typing `ls` in the repository directory, you should see a file called `requirements.txt`. Finally, you can run the following

```
pip install -r requirements.txt
```
* Be patient and wait for the libraries to finish installing

### IBM API token
If you would like to get access to the quantum computers used in this project to run your own simulations, please do the following:
* Go to [quantum-computing.ibm.com](https://quantum-computing.ibm.com)
* Create an IBMid account if you do not have one already and follow the steps to set up your account. If you do, log in to your account.
* Once you have your account, go to the homepage
* On the homepage, you will see a section that says `API token` with a copy icon next to the asterisks. Click on the icon.
* What you have is your own unique API token to retrieve your own job requests to the IBM quantum backend. DO NOT SHARE THIS TOKEN WITH ANYONE!!!
* If there is a section in the files that are listed with a comment mentioning an API token, you may paste your API token to get your own job requests

(*NOTE*) If you run your own simulations, it may take some time until you can get your results back due to the other people requesting to run other quantum simulations. It is in your best interest to go back to the homepage on [quantum-computing.ibm.com](https://quantum-computing.ibm.com) and click on `View all` in the section of the page that says "Run on circuits & programs via IBM Quantum compute resources". Any computer that says "open" under the `Plan` category is a computer that you can run your simulations on. A computer that says "premium" will require you to make a payment to use, though there will be less traffic for these computers. You should make the proper judgement as to which computer you should use to obtain your simulation results.

If you have any questions, please feel free to reach out to Kevin Lie-Atjam (klieatjam@olin.edu) or Mihir Vemuri (mvemuri@olin.edu)
