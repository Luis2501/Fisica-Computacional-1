"""
Caida libre 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

import numpy as np
import sys

sys.path.append("../")

from PhyPy.EulerPy import *

class Sistema_mecanico(Euler):

	def __init__(self, gravedad):
	
		self.Posicion = []
		self.Velocidad = []
		self.tiempo = []
		self.g = gravedad

	def Ec_Diferencial(self, t, x, dx, y, dy, z, dz):

		return np.array([0,-9.8,0])

if __name__=="__main__":

	import matplotlib.animation as animation
	import matplotlib.pyplot as plt

	t, tf, dt, h = 0, 5, 0.01, 100 					 			
	
	posicion, velocidad = np.array([0,h,0]), np.array([0,0,0]) 

	Caida_Libre = Sistema_mecanico(9.81)
	Caida_Libre.Metodo_Euler_Cromer(t, tf, dt, posicion, velocidad)

	plt.title("Caida libre")
	plt.plot(Caida_Libre.tiempo, Caida_Libre.y, label = r"$y(t)$")
	plt.xlabel(r"tiempo (s)")
	plt.ylabel(r"Posicion (m)")
	plt.legend()
	plt.grid()
	plt.show()
