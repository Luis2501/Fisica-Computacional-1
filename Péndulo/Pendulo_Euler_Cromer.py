"""
Péndulo Simple (Método de Euler-Cromer)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mié 03 mar 2021 09:04:54 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Pendulo:

	def __init__(self, g, l, m):

		self.g, self.l, self.m = g, l, m

	def __call__(self, u, t):
	
		theta, vtheta = u  
		g,l = self.g, self.l 
		
		return np.array([vtheta, (-g/l)*theta])

	def Energy(self, theta):

		K = (1/2)*(self.m)*((self.l*theta[:,1])**2) 
		U = (self.m)*(self.g)*(self.l)*(1 - np.cos(theta[:,0]))		
		E = K + U

		return K, U, E


if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Sistema = Pendulo(9.81, 1, 1)						#Instancia en la clase Pendulo (l=1 m, g= 9.81 m/s²)
	
	Solucion = Euler_Cromer(Sistema, System = False)			#Instancia en la clase Euler-Cromer	
	Solucion.InitialConditions([np.pi/18,0], [0,10], 0.001)			#Aplicamos condiciones inciales		
	theta,t = Solucion.SolveODE()						#Soluciones (ángulo = theta[:,0], velocidad = [:,1])

	Solucion1 = Verlet(Sistema, System = False)
	Solucion1.InitialConditions([np.pi/18,0], [0,10], 0.001)
	theta1, t1 = Solucion1.SolveODE()

	#K, U, E = Sistema.Energy(theta)					#Energía del sistema (solo si se requiere) 

	plt.title("Movimiento del péndulo simple")
	plt.plot(t, theta[:,0], label=r"$\theta$ (t)")				#Graficamos theta vs tiempo	
	plt.plot(t1, theta1[:,0])
	plt.xlabel("tiempo (s)") ; plt.ylabel(r"$\theta$ (rad)")		
	plt.grid(True) ; plt.legend()
	plt.show()
