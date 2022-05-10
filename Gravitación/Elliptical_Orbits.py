"""
Movimiento planetario (Órbitas elípticas)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

jue 08 abr 2021 11:37:03 CDT 

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
	
	Planets = ["Venus", "Tierra", "Marte", "Jupiter", "Saturno"]			#Planetas a considerar
	
	a = [0.72, 1, 1.52, 5.21, 9.54]							#Semieje mayor de los planetas en AU

	Time = [0.615, 1, 1.881, 11.862, 29.48]						#Tiempo que tardan en dar una vuelta

	r_1 = [0.718, 0.98, 1.38, 4.95, 9.05]						#Perihelio de los planetas

	r_2 = [0.728, 1.1, 1.66, 5.46, 10.12]						#Afelio de los planetas

	for planet, r, T, r1, r2 in zip(Planets, a, Time, r_1, r_2): 

		Planet = Orbit()							#Definimos el objeto Planeta
		Solution = Euler_Cromer(Planet, System = False)				#Instancia en la clase Euler-Cromer

		v = (2*np.pi*r/T)*np.sqrt((2*r*r2)/(r1*(r1+r2)))

		Condition = [[r1, 0], 							#Posición (x,y)  
		     	     [0, v]]							#Velocidad (Vx, Vy)

		Time = [0, 2*T]								#Tiempo de 0 hasta 1 anio

		Solution.InitialConditions(Condition, Time, 0.001)			#Definimos condiciones iniciales
		u, t = Solution.SolveODE()						#Obtenemos la solución 				

		plt.plot(u[:,0], u[:,1], label = planet)				#Gráfica de la órbita

	plt.title("Órbitas de los planetas")
	plt.xlabel("$x$ (AU)") ; plt.ylabel("$y$ (AU)")
	plt.grid() ; plt.legend() 
	plt.show()
