import qiskit
from qiskit import IBMQ
from qiskit import execute
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram

'''
This programe is create by Sujit Mandal
Github: https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
'''

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)
circuit.draw(output='mpl')
plt.show()

circuit.cx(qr[0], qr[1])
circuit.draw(output='mpl')
plt.show()

circuit.measure(qr, cr)
circuit.draw(output='mpl')
plt.show()
IBMQ.save_account('32e0c0acdb3187227dcd89986fa9c7845c0c5070c6052c92aad5543e837a81ea01334f3bbd9fe7fa724a06326e7dc05008d74798dbba79068a9f1d7635f2d02b')
IBMQ.load_account()

provider = IBMQ.get_provider('ibm-q')
quantum_computer = provider.get_backend('ibmq_16_melbourne')
job = execute(circuit, backend=quantum_computer)
job_monitor(job)

result = job.result()
plot_histogram(result.get_counts(circuit))
plt.show()