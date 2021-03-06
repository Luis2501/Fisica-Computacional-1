import numpy as np 

class RC_Circuit:

	def __init__(self, R, C):

		self.R, self.C = R, C

	def __call__(self, u, t):

		v = u
		R, C = self.R, self.C 

		return -v * (1/(R*C))

if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Circuito = RC_Circuit(3e3, 1e-6)
	
	Solucion = Euler(Circuito)
	Solucion.InitialConditions(1.4, [0,22e-3], 1e-6)
	V, t = Solucion.SolveODE()

	plt.plot(t, V[:,0])
	plt.grid() 
	plt.show()
