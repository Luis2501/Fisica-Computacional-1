"""
Péndulo Simple, Amortiguado y/o Forzado

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

vie 05 mar 2021 22:35:34 CST   

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
from math import sin, sqrt
import numpy as np

class Pendulo_Simple:

	def __init__(self, g, l, m, q, Fd, omega, tipo = None):

		self.g, self.l, self.m = g, l, m
		self.q, self.Fd, self.omega = q, Fd, omega
		self.tipo = tipo

	def __call__(self, u, t):
	
		theta, vtheta = u  
		g,l,  = self.g, self.l 
		q, Fd, omega = self.q, self.Fd, self.omega 

		if self.tipo == "Simple":

			return np.array([vtheta, -g/l*theta])

		elif self.tipo == "Amortiguado":
		
			return np.array([vtheta, -g/l*theta - q*vtheta])

		elif self.tipo == "Forzado": 

			return np.array([vtheta, -g/l*theta - q*vtheta + Fd*sin(omega*t)])

		else:

			raise ValueError("No type of system")

if __name__ == "__main__":
	
	import matplotlib.pyplot as plt
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import *

	q, Fd, omega, Omega = 1, 0.2, 2, np.linspace(0,4, 1001)	 

	Sistema = Pendulo_Simple(9.81, 1, 1, q, Fd, omega, tipo = "Forzado")		#Instancia en la clase Pendulo 
	
	Solucion = Euler_Cromer(Sistema, System = False)				#Instancia en la clase Euler-Cromer	
	Solucion.InitialConditions([np.pi/18,0], [0,20], 0.001)				#Aplicamos condiciones inciales		
	theta,t = Solucion.SolveODE()							#Soluciones (ángulo = theta[:,0], velocidad = [:,1]) 
	
	A = lambda omega_0 : Fd/np.sqrt((omega_0**2 - omega**2)**2 + (omega**2))	#Amplitud en función de la frecuencia natural
	
	print("Ángulo de resonancia = ", A(sqrt(9.81)), "rad")				#Imprimir ángulo de resonancia

	fig, (ax1,ax2) = plt.subplots(1, 2, figsize = (13,13))					
	
	#Gráfica theta vs tiempo
	ax1.set_title("Movimiento del péndulo forzado")
	ax1.plot(t,theta[:,0], label=r"$\theta(t)$")
	ax1.set_xlabel(r"tiempo (s)") ; ax1.set_ylabel(r"$\theta$ (rad)") 
	ax1.legend() ; ax1.grid()
		
	#Gráfica velocidad vs tiempo
	ax2.set_title("Amplitud vs frecuencia")
	ax2.plot(Omega, A(Omega), color = "orange", label = r"$A(\omega)$")
	ax2.set_xlabel(r"$\omega$") ; ax2.set_ylabel(r"$A$")
	ax2.legend() ; ax2.grid()	

	plt.show()
