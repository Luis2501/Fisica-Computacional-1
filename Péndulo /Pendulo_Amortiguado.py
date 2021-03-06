"""
Péndulo Amortiguado

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

jue 04 mar 2021 09:00:29 CST  

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Pendulo_Amortiguado:

	def __init__(self, g, l, m, q):

		self.g, self.l, self.m, self.q = g, l, m, q

	def __call__(self, u, t):
	
		theta, vtheta = u  
		g,l, q = self.g, self.l, self.q 
		
		return np.array([vtheta, -g/l*theta - q*vtheta])

if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	for q in [1,5,10]:

		Sistema = Pendulo_Amortiguado(9.81, 1, 1, q)			#Instancia en la clase Pendulo (l=1 m, g= 9.81 m/s²)
	
		Solucion = Euler_Cromer(Sistema, System = False)		#Instancia en la clase Euler-Cromer	
		Solucion.InitialConditions([np.pi/18,0], [0,10], 0.001)		#Aplicamos condiciones inciales		
		theta,t = Solucion.SolveODE()					#Soluciones (ángulo = theta[:,0], velocidad = [:,1])

		plt.plot(t, theta[:,0], label=r"$q = $" + f"{q}")		#Graficamos theta vs tiempo

	#Ajustes de la gráfica
	plt.title("Movimiento del péndulo amortiguado")
	plt.xlabel("tiempo (s)") ; plt.ylabel(r"$\theta$ (rad)")		
	plt.grid(True) ; plt.legend()
	plt.show()
