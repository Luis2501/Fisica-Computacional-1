"""
Movimiento rectilineo uniforme 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

vie 12 feb 2021 09:09:59 CST 
"""

import numpy as np

class MRU:

	def __init__(self, v):

		self.v = v

	def __call__(self, u, t):

		x = u
		v = self.v

		return v

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	v = 40									#Velocidad 

	Sistema = MRU(v)							

	Solucion = Euler(Sistema)						#Instancia para método de Euler
	Solucion.InitialConditions(0, [0,4], 0.01)				#Definición de condiciones inciales
	x,t = Solucion.SolveODE()						#Solución numérica
	
	x_sol = v*t								#Solución analítica

	#Gráfica
	plt.title("Movimiento rectilineo uniforme")
	plt.plot(t, x[:,0], label = r"Solución numérica")
	plt.plot(t, x_sol, label = r"Solución analítica")
	plt.xlabel(r"tiempo (s)") ; plt.ylabel(r"Posicion (m)")
	plt.legend() ; plt.grid() ; plt.show()
