"""
Circuito RC (Clase y solución para distintas frecuencas)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mié 10 mar 2021 09:12:48 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np
import sys
sys.path.append("../")
from PhysicsPy.ODEsMethods import *

class RC_Circuit:

	"""
	Clase que permite resolver un circuito RC,
	tanto para una fuente de voltaje alterna
	como fuente de voltaje directa.
	"""

	def __init__(self, R, C, Vs):

		self.R, self.C = R, C

		if isinstance(Vs, (int, float)):

			self.Vs = lambda t: Vs						#Voltaje para corriente directa, 
											#El circuito es estacionario si Vs = 0

		elif callable(Vs): 

			self.Vs = Vs							#Fuente de voltaje alterno

		else: 

			raise ValueError("Voltage is not defined")			#No se definio algún tipo de voltaje

	def __call__(self, u, t):

		Q = u
		R, C = self.R, self.C 
		Vs = self.Vs

		return (Vs(t)/R) - (Q/(R*C))


def SolveCircuit(frecuencia, Periodo, R, C):

	"""
	Función que resuelve el circuito para distintas 
	frecuencias de una fuenta de voltaje.
	"""

	QQ, tt, VVs = [], [], []

	for f, T in zip(frecuencia, Periodo): 

		Vs = lambda t: np.cos((2*np.pi*f)*t)					#Fuente de voltaje
    
		Circuito = RC_Circuit(R, C, Vs)						#Instancia, creamos un circuito

		Solucion = Euler(Circuito)						#Resolvemos con el método de Euler
		Solucion.InitialConditions(1e-6, [0, 2*T], (1/f)*1e-3)			#Condiciones iniciales
		Q, t = Solucion.SolveODE()						#Obtenemos la solución
    
		QQ.append(Q[:,0]) ; tt.append(t)
		VVs.append(Vs(t))

	return QQ, tt, VVs	

