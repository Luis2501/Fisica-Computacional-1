import numpy as np 

class RC_Circuit:

	def __init__(self, R, C, L, Serie = True):

		self.R, self.C, self.L = R, C, L
		self.Serie = Serie

	def __call__(self, u, t):

		i, di = u
		R, C, L = self.R, self.C, self.L 

		if self.Serie: 

			return np.array([di, -((R*di)/(L)) - ((i)/(L*C)) ])

		else: 

			return 0

if __name__ == "__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Circuito = RC_Circuit(3e3, 1e-6)
	
	Solucion = Euler(Circuito)
	Solucion.InitialConditions(1.4, [0,22e-3], 1e-6)
	V, t = Solucion.SolveODE()

	plt.title("Circuito RLC")
	plt.plot(t, V[:,0])
	plt.grid() ; plt.show()
