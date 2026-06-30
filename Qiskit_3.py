# %%

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit.result import marginal_distribution
from qiskit.circuit.library import UGate
from math import pi
import random 


Qubit = QuantumRegister(1 , "Q") 

qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0,1) 

qc2.draw("latex")


