"""
Gravitación de Newton (Problema de dos cuerpos y tres cuerpos)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mar 23 mar 2021 09:18:25 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Orbit:

	def __init__(self, Ms, Mp0, Mp1, NumBodies):

		if Ms == 0:

			self.GM = 4*(np.pi**2)

		else: 

			self.GM = 4*(np.pi**2)
			self.GMp0, self.GMp1 = self.GM*(Mp0/Ms), self.GM*(Mp1/Ms)

		self.NumBodies = NumBodies

	def __call__(self, u, t):

		if self.NumBodies == 2:

			x, y, vx, vy = u 
			GM, r = self.GM, (np.sqrt(x**2 + y**2))**3

			return np.array([vx, vy, (GM*x)/r, (GM*y)/r])

		elif self.NumBodies == 3:

			x0, y0, x1, y1, vx0, vy0, vx1, vy1 = u 

			GM, r0 = self.GM, (np.sqrt(x0**2 + y0**2))**3
			GMp0, r01 = self.GMp0, (np.sqrt((x0 - x1)**2 + (y0 - y1)**2))**3
			GMp1, r1 = self.GMp1, (np.sqrt(x1**2 + y1**2))**3

			return np.array([vx0, vy0, vx1, vy1, 
					-(GM*x0)/(r0) - (GMp0*(x0 - x1))/(r01), 
					-(GM*y0)/(r0) - (GMp0*(y0 - y1))/(r01), 
					-(GM*x1)/(r1) - (GMp1*(x1 - x0))/(r01), 
					-(GM*y1)/(r1) - (GMp1*(y1 - y0))/(r01) ])
