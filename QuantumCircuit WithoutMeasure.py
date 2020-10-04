from qiskit import Aer
from qiskit import execute
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit.tools.visualization import plot_state_city

'''
This programe is create by Sujit Mandal
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
'''

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)

simulator = Aer.get_backend('statevector_simulator')

result = execute(circuit, simulator).result()
statevector = result.get_statevector(circuit)
plot_state_city(statevector, title='Bell state')
plt.show()