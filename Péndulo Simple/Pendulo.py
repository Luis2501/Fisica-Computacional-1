"""
Péndulo Simple 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""
from math import sin
import numpy as np
import sys

sys.path.append("../")

from PhyPy.EulerPy import *

class Sistema_mecanico(Euler):

	def __init__(self, l, g):
	
		self.Posicion = []
		self.Velocidad = []
		self.tiempo = []
		self.l = l 
		self.g = g

	def Ec_Diferencial(self, t, x, dx, y, dy, z, dz):

		return np.array([-(self.g/self.l)*sin(x), 0, 0])

if __name__ == "__main__":

	import matplotlib.pyplot as plt
		
	t, tf, dt, theta_i = 0, 30, 1e-1, np.pi/8

	posicion, velocidad = np.array([theta_i,0,0]), np.array([0,0,0])

	Pendulo = Sistema_mecanico(l = 10, g = 9.8)
	Pendulo.Metodo_Euler_Cromer(t,tf,dt,posicion,velocidad)

	plt.title("Péndulo simple")
	plt.plot(Pendulo.tiempo, Pendulo.x, label = r"$\theta (t)$")
	plt.xlabel(r"tiempo (s)")
	plt.ylabel(r"Posicion (rad)")
	plt.legend()
	plt.grid()
	plt.show()
