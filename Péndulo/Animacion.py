"""
Péndulo Simple. Este archivo es unicamente para generar la animación.

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

vie 26 feb 2021 08:50:46 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
Pagina web personal: https://luis2501.github.io/Programas/Pendulo-Simple.html
"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from Pendulo_Simple import Pendulo
from Pendulo_Amortiguado import Pendulo_Amortiguado
import numpy as np
import sys
sys.path.append("../")
from PhysicsPy.ODEsMethods import *					

def update(i):

	ax.clear()
	
	#plt.plot(np.sin(theta[i,0]), -1*np.cos(theta[i,0]) ,"ro" , color = "red", label = "t = " + str(round(t[i],3)) + " s")
	
	for l in range(len(L)):
	
		plt.plot([0, L[l]*np.sin(Theta[l][i,0])],[0,-L[l]*np.cos(Theta[l][i,0])],"b-", color = "gray")
		plt.plot(L[l]*np.sin(Theta[l][i,0]), -L[l]*np.cos(Theta[l][i,0]) ,"o")
	
	plt.grid() #; plt.legend()
	plt.xlim(-0.5,0.5) ; plt.ylim(-0.4,0)

if __name__ == "__main__":

	L = [0.275, 0.285, 0.296, 0.307, 0.319, 0.331, 0.344]
	Theta, T = [], []

	for l in L:

		Sistema = Pendulo(9.81, 1, l)
	
		Solucion = Euler_Cromer(Sistema, System = False)			#Instancia en el método de Euler-Cromer	
		Solucion.InitialConditions([np.pi/18,0], [0,10], 0.05)			#Condiciones theta = 10°
		theta, t = Solucion.SolveODE()
		
		Theta.append(theta)
		T.append(t)
		
		del Sistema, Solucion, theta, t

	fig = plt.figure()
	ax = fig.gca()
	
	ani = animation.FuncAnimation(fig, update, range(len(T[0])), interval = 1)
	#ani.save("Pendulo_EulerCromer.mp4", fps= 20)				#Este comando guarda la animación
	plt.show()
