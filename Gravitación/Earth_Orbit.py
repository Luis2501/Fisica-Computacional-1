"""
Movimiento planetario (Tierra) 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mié 17 mar 2021 09:02:40 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Orbit:
	
	"""
	Clase que permité calcular las órbitas
	de cualquier planeta.
	"""

	def __init__(self):

		self.GM = -4*(np.pi**2)

	def __call__(self, u, t):	

		x, y, vx, vy = u 
		GM, r = self.GM, (np.sqrt(x**2 + y**2))**3

		return np.array([vx, vy, (GM*x)/r, (GM*y)/r])

if __name__ == "__main__":

	import sys
	sys.path.append("../") 
	import matplotlib.pyplot as plt
	from PhysicsPy.ODEsMethods import *
	
	Earth = Orbit()									#Definimos el objeto Tierra
	
	Solution = method(Earth, System = False)					#Instancia en la clase Euler-Cromer

	Condition = [[1,       0], 							#Posición (x,y)  
		     [0, 2*np.pi]]							#Velocidad (Vx, Vy)

	Time = [0,1]									#Tiempo de 0 hasta 1 anio

	Solution.InitialConditions(Condition, Time, 0.001)				#Definimos condiciones iniciales
	u, t = Solution.SolveODE()							#Obtenemos la solución 					

	#Gráfica de la órbita
	plt.style.use("seaborn")
	plt.title("Órbita de la Tierra")
	plt.plot(u[:,0], u[:,1], label = name)
	plt.xlabel("$x$ (AU)") ; plt.ylabel("$y$ (AU)")
	plt.grid(True) ; plt.show()
