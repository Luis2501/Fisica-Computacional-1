"""
Movimiento con fricción: paracaídas

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mié 17 feb 2021 09:05:37 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1 
"""
import numpy as np

class Movimiento_friccion:

	"""
	Ecuación diferencial 

	dv/dt = a - bv 
	"""

	def __init__(self, a, b):

		self.a, self.b = a, b

	def __call__(self, u, t):

		v, a, b = u, self.a, self.b 

		return a - b*v

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *	
		
	Sistema = Movimiento_friccion(10, 1)				#Instancia en la clase con valores a = 10, b=1

	Solucion = Euler(Sistema)					#Instancia para resolver con Met. Euler
	Solucion.InitialConditions(0, [0,10], 0.01)			#Definición de condiciones inciales
	v_x,t = Solucion.SolveODE()					#Solución numérica

	v_x_sol = Sistema.a - (Sistema.a)*np.exp(-t)			#Solución Analítica

	#Gráfica
	plt.title("Movimiento con fricción: paracaídas")
	plt.plot(t, v_x[:,0], label = "Solución analítica")
	plt.plot(t, v_x_sol, label = "Solución numérica")
	plt.xlabel("tiempo (s)")
	plt.ylabel("Velocidad (m/s)")
	plt.legend() ; plt.grid()
	plt.show()
