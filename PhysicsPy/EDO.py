"""
Luis Eduardo Sánchez González

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas

mié 03 feb 2021 13:10:46 CST 
"""

import numpy as np

class EDO():

	"""
	Solves ODE on the form:
	
	U' = f(u,t)

	with of initial condition u(t0) = U0

	"""

	def __init__(self, f):

		self.f = f

	def __str__(self):

		return f"""Condition initial is: {self.U0} \nTime points is: {self.N}
		       """

	def condiciones_iniciales(self, U0, Deltat, dt):

		"""
		U0 is initial condition 

		U0 = [[  q_1,  q_2,  q_3 ]
		      [ q'_1, q'_2, q'_3 ]]
					
			q_i is generalized coordinate and
			q'_i is generalized velocity
		"""
	
		self.N = int( (Deltat[1] -Deltat[0] ) / dt)
		self.t = np.linspace(Deltat[0], Deltat[1] , self.N +1)

		if isinstance(U0, (int, float)):
	
			self.numero_eqns_dif = 1
			self.numero_coord = 1
			U0 = float(U0)

		else:
	
			self.numero_eqns_dif = len(U0)
				
			if isinstance(U0[0], np.ndarray):

				self.numero_coord = len(U0[0])
			
			else:

				self.numero_coord = 1

			U0 = np.array(U0)

		self.U0 = U0

	def SolveEDO(self):

		n = (self.numero_eqns_dif)*(self.numero_coord)
		self.U = np.zeros((len(self.t), n))

		self.U[0,:] = self.U0

		#Integration	
		for i in range(self.N):
			self.i = i 
			self.U[i + 1] = self.advance()

		return self.U, self.t


class Euler(EDO):
	
	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		return u[i, :] + dt * f(u[i, :], t[i])

class Verlet(EDO):

	def advance(self):

		u, f, i, t = self.u, self.f, self.i, self.t

		if self.i == 0:

			return u[i, :] + f(u[i,:], t[i])*dt 

		else:

			return 2*(self.u[i,:]) - self.u[i-1, :] + f(u[i,:] , t[i])*(dt**2)
