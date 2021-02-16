"""
Movimiento rectilineo uniforme acelerado

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mar 16 feb 2021 08:44:23 CST 
"""

import numpy as np

class MRUA:

	"""
	Ecuación diferencial 

	dv/dt = -g 
	"""

	def __init__(self, g):

		self.g = g

	def __call__(self, u, t):

		v, g = u, self.g 

		return -g

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	g = 9.81								#Aceleración	
		
	Sistema = MRUA(g)														
	Solucion = Euler(Sistema)						#Instancia para método de Euler

	tam_pasos = [1,0.5, 0.1,0.05]						#Tamaños de pasos

	#Gráfica
	for k,m in zip(tam_pasos, range(4)):

		Solucion.InitialConditions(0, [0,10], k)			#Definición de condiciones inciales
		v_x,t = Solucion.SolveODE()					#Solución numérica
		v_x_sol = -g*t							#Solución analítica

		plt.subplot(2, 2, m+1)
		plt.plot(t, v_x[:,0], "o", label = "Sol. dt = " + str(k))
		plt.plot(t, v_x_sol, color= "red", label = r"Sol. Analítica")

		if m > 1: 
			plt.xlabel("tiempo (s)")
		if m==0 or m==2:
			plt.ylabel("Velocidad (m/s)")

		plt.legend() ; plt.grid()
	
	plt.show()
