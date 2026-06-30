# %%
from qiskit.visualization import array_to_latex , plot_histogram
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import Operator
from IPython.display import display
import numpy as np 
from qiskit import QuantumCircuit 

ket0 = Statevector([1,0])

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.s(0)
circuit.y(0)

v = ket0.evolve(circuit)

statistics = v.sample_counts(4000)

display(plot_histogram(statistics))


# %%
