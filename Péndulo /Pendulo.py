"""
Péndulo Simple

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

vie 26 feb 2021 08:50:46 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
Pagina web personal: https://luis2501.github.io/Programas/Pendulo-Simple.html
"""
import numpy as np

class Pendulo:

	def __init__(self, g, l):

		self.g, self.l = g, l

	def __call__(self, u, t):
	
		theta, vtheta = u  
		g,l = self.g, self.l 
		
		return np.array([vtheta, -g/l*theta])

	def Energy(self, theta):

		K, U = (1/2*1)*(theta[:,1])**2,  1*Sistema.g*(1 - np.cos(theta[:,0]))
		E = K + U

		return K, U, E

if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	from ODEsSolver import *

	Sistema = Pendulo(9.81,1)						#Instancia en la clase Pendulo (l=1 m, g= 9.81 m/s²)
		
	Solucion = Euler(Sistema)						#Resolvemos mediante el método de Euler
	Solucion.InitialConditions([np.pi/18,0], [0,10], 0.01)			#Aplicamos condiciones inciales
	theta,t = Solucion.SolveODE()						#Soluciones (ángulo = theta[:,0], velocidad = [:,1])

	#K, U, E = Sistema.Energy(theta)					#Energía del sistema (solo si se requiere) 

	plt.title("Movimiento del péndulo simple")
	plt.plot(t, theta[:,0], label=r"$\theta$ (t)")				#Graficamos theta vs tiempo	
	plt.xlabel("tiempo (s)") ; plt.ylabel(r"$\theta$ (rad)")		
	plt.grid(True) ; plt.legend()
	plt.savefig("Avst.png")
	plt.show()
