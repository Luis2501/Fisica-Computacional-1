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
	from PhysicsPy.EDO import *

	Sistema = Caida_libre(9.8)

	solver = Euler(Sistema)
	solver.condiciones_iniciales([100,0], [0,4], 0.01)
	y,t = solver.Solve()		

	solver1 = Verlet(Sistema)
	solver1.condiciones_iniciales([100,0], [0,4], 0.01)
	y1,t1 = solver.Solve()
	
	help(SolveODE)
	print("Error entre los métodos: ", np.mean(abs(y1[:,0] - y[:,0])*100))

	plt.title("Caida libre")
	plt.plot(t, y[:,0], label = r"Euler")
	plt.plot(t1, y1[:,0], label = r"Verlet")
	plt.xlabel(r"tiempo (s)") ; plt.ylabel(r"Posicion (m)")
	plt.legend() ; plt.grid() ; plt.show()
