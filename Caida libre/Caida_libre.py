"""
Caida libre 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

import numpy as np

class Caida_libre:

	def __init__(self, g):

		self.g = g

	def __call__(self, u, t):

		y, vy = u
		g = self.g

		return np.array([vy, -g])

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Sistema = Caida_libre(9.8)

	solver = Euler(Sistema)
	solver.InitialConditions([100,0], [0,4], 0.01)
	y,t = solver.SolveODE()			

	solver1 = Euler_Cromer(Sistema)
	solver1.InitialConditions([100,0], [0,4], 0.01)
	y1,t1 = solver1.SolveODE()	
	
	plt.title("Movimiento en caida libre")
	plt.plot(t, y[:,0], label = r"$y(t)$")
	plt.plot(t1, y1[:,0], label = r"$y(t)$")
	plt.xlabel(r"tiempo (s)") ; plt.ylabel(r"Posicion (m)")
	plt.legend() ; plt.grid() ; plt.show()
