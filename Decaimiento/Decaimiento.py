"""
Decaimiento radiactivo 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

jue 11 feb 2021 08:17:01 CST 
"""
import numpy as np

class Decaimiento:

	def __init__(self, tau):

		self.tau = tau

	def __call__(self, u, t):

		N, tau = u, self.tau

		return -N/tau

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	Nucleos = Decaimiento(1)
	N0 = 100	

	Solucion = Euler(Nucleos)
	Solucion.InitialConditions(N0, [0,5], 0.05)
	N, t = Solucion.SolveODE()					

	Nu = N0*np.exp(-t/Nucleos.tau)

	plt.title("Decaimiento radiactivo")
	plt.plot(t, N[:,0], label = r"Solución numérica")
	plt.plot(t, Nu, label = "Solución analítica")
	plt.xlabel(r"Tiempo (seg)") 
	plt.ylabel(r"Número de núcleos")
	plt.legend() ; plt.grid() ; plt.show()
