"""
Luis Eduardo Sánchez González

Miercoles 2 de diciembre de 2020
"""
from numpy import array
from PhyPy.EulerPy import * 
from PhyPy.RungeKuttaPy import * 
from PhyPy.VerletPy import * 
from math import cos, sin, pi, tan, exp, sqrt

class Sistema_fisico(Euler, Verlet, Runge_Kutta):

	def __init__(self, Ecuaciones):

		self.Ecuaciones = Ecuaciones 
		self.Posicion = []
		self.Velocidad = []
		self.tiempo = []

	def __str__(self):

		Descripcion = """\nEcuaciones de movimiento: 
				\n\nx''(t) = {} \ny''(t) = {} \nz''(t) = {} \n
				""".format(self.Ecuaciones[0], self.Ecuaciones[1], self.Ecuaciones[2]) 

		return Descripcion

	def Ec_Diferencial(self, t=None, x=None, dx=None, y=None, dy=None, z=None, dz=None):

		Evaluacion = array([float(eval(self.Ecuaciones[0])), 
				    float(eval(self.Ecuaciones[1])), 
				    float(eval(self.Ecuaciones[2]))])
		return Evaluacion

	def Obtener_Momento(self):
	
		try: 
			self.P_x = (self.masa)*(self.V_x)
			self.P_y = (self.masa)*(self.V_y)
			self.P_z = (self.masa)*(self.V_z)
		except:
			print("La velocidad aún no se ha definido")

