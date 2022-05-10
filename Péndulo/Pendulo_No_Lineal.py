"""
Péndulo No lineal

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

lun 08 mar 2021 09:40:23 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Pendulo:

	def __init__(self, g, l, m):

		self.g, self.l, self.m = g, l, m

	def __call__(self, u, t):
	
		theta, vtheta = u  
		g,l = self.g, self.l 
		
		return np.array([vtheta, -g/l*np.sin(theta)])

if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Sistema = Pendulo(9.81, 1, 1)						#Instancia en la clase Pendulo (l=1 m, g= 9.81 m/s²)
	
	for i in range(55,95,10):

		Solucion = Euler_Cromer(Sistema, System = False)			#Instancia en la clase Euler-Cromer	
		Solucion.InitialConditions([np.radians(i),0], [0,10], 0.001)		#Aplicamos condiciones inciales		
		theta,t = Solucion.SolveODE()						#Soluciones (ángulo = theta[:,0], velocidad = [:,1])

		plt.plot(t, theta[:,0], label=r"$\theta$ = " + f"{i} °")		

	plt.title("Movimiento del péndulo no lineal")	
	plt.xlabel("tiempo (s)") ; plt.ylabel(r"$\theta$ (rad)")		
	plt.grid(True) ; plt.legend()
	plt.show()
