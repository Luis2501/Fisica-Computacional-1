"""
Problema de los tres cuerpos (Sol-Tierra-Luna)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mar 23 mar 2021 09:18:25 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np
from Gravitation import Orbit
import matplotlib.pyplot as plt	

if __name__ == "__main__":

	import sys
	sys.path.append("../") 
	from PhysicsPy.ODEsMethods import *
	
	re, rl = 1, 0.99743								#Radio de la Tierra y de la luna
	Ms, Ml, Me = 1.989e30, 7.35e22, 5.972e24					#Masa del Sol, Luna y Tierra
	ve = 2*np.pi 									#Velocidad de la Tierra y Luna
	vl = 2*np.pi*np.sqrt(Me/(Ms*(re-rl))) 
	vl = vl + ve 

	Earth_Moon = Orbit(Ms, Ml, Me, NumBodies = 3)					#Definimos el objeto Tierra-Luna
	Solution = Euler_Cromer(Earth_Moon, System = False)				#Instancia en la clase Euler-Cromer

	Condition = [[re, 0, rl, 0], 							#Posición (xe, ye, xl, yl)  
		     [0, ve, 0, vl]]							#Velocidad (Vxe, Vye, Vxl, Vyl)

	Time = [0, 1]									#Tiempo de 0 hasta 1 anio

	Solution.InitialConditions(Condition, Time, 1e-5)				#Definimos condiciones iniciales
	u, t = Solution.SolveODE()							#Obtenemos la solución 				

	#Gráfica de las órbitas
	plt.title("Sistema Sol-Tierra-Luna")
	plt.plot(0, 0, "o", color = "yellow", label = "Sol")
	plt.plot(u[:,0], u[:,1], label = "Tierra")
	plt.plot(u[:,2], u[:,3], color="gray", label = "Luna")
	plt.xlabel("$x$ (AU)") ; plt.ylabel("$y$ (AU)")
	plt.grid() ; plt.legend()
	plt.show()
