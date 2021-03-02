import json
import qiskit as q
import numpy as np
import matplotlib.pyplot as plt


print('Qiskit Version :')
print(json.dumps(q.__qiskit_version__, indent=3))

Psi = np.array([[0],[0],[1],[0]])
print('\n')
print('PSI :')
print(Psi)

Phi = np.array([[0],[0],[0],[1]])
print('\n')
print('PHI :')
print(Phi)

q0 = np.array([[1],[0]])
q1 = np.array([[1],[0]])
q2 = np.array([[0],[1]])
q3 = np.array([[1],[0]])

tensorProduct1 = np.kron(q0,q1)
tensorProduct2= np.kron(q2,q3)
tensorProductPsi = np.kron(tensorProduct1,tensorProduct2)
print('\n')
print('Tensor Product Psi :')
print(tensorProductPsi)


CNOT = np.array([[1, 0, 0, 0],[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
I = np.array([[1, 0],[0, 1]])
tensorProductI = np.kron(I,I)
U = np.kron(tensorProductI,CNOT)
print('\n')
print('Tensor Product U :')
print(U)


## statevector of Phi
statevectorPhi = np.dot(U, tensorProductPsi)
print('\n')
print('statevector of Phi :')
print(statevectorPhi)