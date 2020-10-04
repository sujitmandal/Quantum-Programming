from qiskit import Aer
from qiskit import execute
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit.tools.visualization import plot_histogram

'''
This programe is create by Sujit Mandal
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
'''

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, simulator).result()
counts = result.get_counts(circuit)
plot_histogram(counts, title='Bell-State counts')
plt.show()