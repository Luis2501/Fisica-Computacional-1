"""
Problema de los tres cuerpos (Sol-Tierra-Jupiter)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mar 23 mar 2021 09:18:25 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Orbit:

	def __init__(self, Ms, Mp0, Mp1):

		self.GM = 4*(np.pi**2)
		self.GMp0, self.GMp1 = self.GM*(Mp0/Ms), self.GM*(Mp1/Ms)

	def __call__(self, u, t):	

		x0, y0, x1, y1, vx0, vy0, vx1, vy1 = u 

		GM, r0 = self.GM, (np.sqrt(x0**2 + y0**2))**3
		GMp0, r01 = self.GMp0, (np.sqrt((x0 - x1)**2 + (y0 - y1)**2))**3
		GMp1, r1 = self.GMp1, (np.sqrt(x1**2 + y1**2))**3

		return np.array([vx0,	vy0,	vx1,	vy1, 
				-(GM*x0)/(r0) - (GMp0*(x0 - x1))/(r01), 
				-(GM*y0)/(r0) - (GMp0*(y0 - y1))/(r01), 
				-(GM*x1)/(r1) - (GMp1*(x1 - x0))/(r01), 
				-(GM*y1)/(r1) - (GMp1*(y1 - y0))/(r01) ])

if __name__ == "__main__":

	import sys
	sys.path.append("../") 
	import matplotlib.pyplot as plt	
	from PhysicsPy.ODEsMethods import *
	
	re, rj = 1, 5.2									#Radio de la Tierra y de Jupiter
	ve, vj = 2*np.pi, (2*np.pi*rj)/(11.86)						#Velocidad de la Tierra y Jupiter
	Ms, Mj, Me = 2e30, 1.9e27, 6e24							#Masa del Sol, Jupiter y Tierra

	Earth_Jupiter = Orbit(Ms, k*Mj, Me)						#Definimos el objeto Tierra-Jupiter
	Solution = Euler_Cromer(Earth_Jupiter, System = False)				#Instancia en la clase Euler-Cromer

	Condition = [[re, 0, rj, 0], 							#Posición (xe, ye, xj, yj)  
		     [0, ve, 0, vj]]							#Velocidad (Vxe, Vye, Vxj, Vyj)

	Time = [0, 12]									#Tiempo de 0 hasta 12 anios

	Solution.InitialConditions(Condition, Time, 0.001)				#Definimos condiciones iniciales
	u, t = Solution.SolveODE()							#Obtenemos la solución 				

	#Gráfica de las órbitas
	plt.title("Sistema Sol-Tierra-Jupiter")
	plt.plot(0, 0, "o", color = "yellow", label = "Sol")
	plt.plot(u[:,0], u[:,1], label = "Tierra")
	plt.plot(u[:,2], u[:,3], label = "Jupiter")
	plt.xlabel("$x$ (AU)") ; plt.ylabel("$y$ (AU)")
	plt.grid() ; plt.legend()
	plt.show()
