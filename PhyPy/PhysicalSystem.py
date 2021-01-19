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

	def __init__(self, Ecuaciones, Masa = None):

		self.Ecuaciones = Ecuaciones 
		self.masa = Masa
		self.Posicion = []
		self.Velocidad = []				 
		self.Momento = [] 		
		self.tiempo = []

	def __str__(self):

		return """\nEcuaciones de movimiento: \n\nẍ = {} \nÿ = {} \nz = {} \n""".format(self.Ecuaciones[0], self.Ecuaciones[1], self.Ecuaciones[2]) 

	def Ec_Diferencial(self, t=None, x=None, dx=None, y=None, dy=None, z=None, dz=None):

		return array([float(eval(self.Ecuaciones[0])), float(eval(self.Ecuaciones[1])), float(eval(self.Ecuaciones[2]))])

	def Obtener_Momento(self):
	
		try: 
			self.P_x = (self.masa)*(self.V_x)
			self.P_y = (self.masa)*(self.V_y)
			self.P_z = (self.masa)*(self.V_z)
		except:
			print("La velocidad aún no se ha definido")

	def Energia_Sistema(self, Energia_Potencial):

		self.Energia_Cinetica = (1/2)*(self.masa)*((self.V_x)**2 + (self.V_y)**2 + (self.V_z)**2)**2	
		self.Energia_Potencial = Energia_Potencial

		self.Energia_total = self.Energia_Cinetica + self.Energia_Potencial
