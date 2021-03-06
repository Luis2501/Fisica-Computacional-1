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

def update(i):

	ax.clear()
	plt.plot([0, np.sin(theta[i,0])],[0,-1*np.cos(theta[i,0])],"b-", color = "black")
	plt.plot(np.sin(theta[i,0]), -1*np.cos(theta[i,0]) ,"ro" , color = "red", label = "t = " + str(round(t[i],3)) + " s")
	plt.grid() ; plt.legend()
	plt.xlim(-1,1) ; plt.ylim(-1.5,0)

if __name__ == "__main__":

	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	#Sistema = Pendulo(9.81,1,1)						#Pendulo con l=1, g=9.81m/s², m= 1 kg
	Sistema = Pendulo_Amortiguado(9.81,1,1,1)
		
	#Solucion = Euler(Sistema)						#Instancia en el método de Euler
	Solucion = Euler_Cromer(Sistema, System = False)			#Instancia en el método de Euler-Cromer	
	Solucion.InitialConditions([np.pi/18,0], [0,10], 0.05)			#Condiciones theta = 10°
	theta,t = Solucion.SolveODE()						

	fig = plt.figure()
	ax = fig.gca()
	
	ani = animation.FuncAnimation(fig, update, range(len(t)), interval = 1)
	#ani.save("Pendulo_EulerCromer.mp4", fps= 20)				#Este comando guarda la animación
	plt.show()
