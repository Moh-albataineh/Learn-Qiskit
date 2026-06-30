# %%
from qiskit.visualization import array_to_latex
from qiskit.quantum_info import Statevector
from IPython.display import display
import numpy as np 

M1 = np.array([[1,1],[0,0]])
M2 = np.array([[1,0],[0,1]])

u = Statevector([1/np.sqrt(2),1/np.sqrt(2)])
v = Statevector([(1+2.0j)/3 , -2/3])
w = Statevector([1/3 , 2/3])


M =  M1/2 + M2/2

display(u.draw("text"))
display(u.draw("latex"))
print(u.draw("latex_source"))
