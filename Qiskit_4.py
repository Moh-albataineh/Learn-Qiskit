# %%
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit.result import marginal_distribution
from qiskit.circuit.library import UGate
from math import pi
from IPython.display import display
import random



qubit = QuantumRegister(1 , "Q")
ebit0 = QuantumRegister(1 , "A")
ebit1 = QuantumRegister(1 , "B")

a = ClassicalRegister (1 , "a")
b = ClassicalRegister(1 , "b")

protocol = QuantumCircuit(qubit , ebit0 , ebit1 , a , b)

# phi (Alic and Bob)
protocol.h(ebit0)
protocol.cx(ebit0 , ebit1)
protocol.barrier()

# Alice operetors
protocol.cx(qubit , ebit0)
protocol.h(qubit)
protocol.barrier()

#Alice measure the qubits and give the Classical bet to Bob
protocol.measure(ebit0 , a)
protocol.measure(qubit , b)
protocol.barrier()

#Bob operetors after the classical bit

with protocol.if_test((a , 1)):
    protocol.x(ebit1)
    
with protocol.if_test((b , 1)):
    protocol.z(ebit1)


display(protocol.draw(output="mpl"))  



