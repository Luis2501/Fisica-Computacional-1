"""
Caminata aleatoria unidimensional (Promedios estadísticos)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

jue 15 abr 2021 09:55:53 CDT  

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("../")
from PhysicsPy.Random_Walk import Random_Walk_1D

Walkers = Random_Walk_1D(0.5, 100)
steps = Walkers.Multiple_Walkers(100)

distances = np.zeros(len(steps))

for i in range(len(steps[0])):

	distances += (1/len(steps[0]))*(steps[:,i]**2)
	
plt.title("Caminatas aleatorias")
plt.plot(distances, label = r"$\langle x^2 \rangle \; vs \; t$ ")		
plt.xlabel("tiempo (Pasos)") ; plt.ylabel(r"$\langle x^2 \rangle $")
plt.legend() ; plt.grid()	
plt.show()	
