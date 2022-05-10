"""
Movimiento planetario (Comprobación Tercera ley de Kepler) 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

jue 18 mar 2021 09:05:20 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Orbit:
	
	"""
	Clase que permité calcular las órbitas
	de cualquier planeta.
	"""

	def __init__(self, Planet, Radius):

		self.GM = -4*(np.pi**2)
		self.Planet, self.Radius = Planet, Radius

	def __str__(self):

		return f"Planet: {self.Planet} \nRadius: {self.Radius} AU"

	def __call__(self, u, t):	

		x, y, vx, vy = u 
		GM, r = self.GM, (np.sqrt(x**2 + y**2))**3

		return np.array([vx, vy, (GM*x)/r, (GM*y)/r])

	def Kepler_Third_Law(self, x, y, t):
		
		r = np.sqrt(x**2 + y**2)
				
		return round(T**2/(np.mean(r) **3), 4)	

if __name__ == "__main__":

	import sys
	sys.path.append("../") 
	import matplotlib.pyplot as plt
	from PhysicsPy.ODEsMethods import *
	
	Planets = ["Venus", "Earth", "Mars", "Jupyter", "Saturn"]			#Planetas a considerar
	
	Radius = [0.72, 1, 1.52, 5.2, 9.54]						#Radio de los planetas en AU

	Time = [0.61, 1, 1.88, 11.86, 29.47]						#Tiempo que tardan en dar una vuelta

	for planet, r, T in zip(Planets, Radius, Time): 

		Planet = Orbit(planet, r)						#Definimos el objeto Planeta
		Solution = Euler_Cromer(Planet, System = False)				#Instancia en la clase Euler-Cromer

		Condition = [[r,       0], 						#Posición (x,y)  
		     	     [0, (2*np.pi*r)/T]]					#Velocidad (Vx, Vy)

		Time = [0, T]								#Tiempo de 0 hasta 1 anio

		Solution.InitialConditions(Condition, Time, 0.001)			#Definimos condiciones iniciales
		u, t = Solution.SolveODE()						#Obtenemos la solución 					

		print(Planet)								#Características del planeta

		Result = Planet.Kepler_Third_Law(u[:,0], u[:,1], T)			#Determinamos T²/r³
		print("T²/r³:", Result, "yr²/AU³", "\n")

		plt.plot(u[:,0], u[:,1], label = planet)				#Gráfica de la órbita

	plt.title("Órbitas de los planetas")
	plt.xlabel("$x$ (AU)") ; plt.ylabel("$y$ (AU)")
	plt.grid() ; plt.legend() 
	plt.show()
