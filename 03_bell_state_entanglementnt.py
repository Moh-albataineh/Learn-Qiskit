from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

qr = QuantumRegister(2, name="q")
cr = ClassicalRegister(2, name="c")
circuit = QuantumCircuit(qr, cr)

circuit.h(0)
circuit.cx(0, 1)

circuit.measure(qr, cr)

print("--- Quantum Circuit ---")
display(circuit.draw(output='mpl'))

simulator = AerSimulator()
job = simulator.run(circuit, shots=1000) 
result = job.result()
counts = result.get_counts(circuit)

print("\n--- Measurement Results ---")
print(counts)
display(plot_histogram(counts, title="Bell State Probabilities"))
