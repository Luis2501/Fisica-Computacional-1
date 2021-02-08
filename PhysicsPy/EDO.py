"""
Luis Eduardo Sánchez González

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas

mié 03 feb 2021 13:10:46 CST 
"""

import numpy as np

class SolveODE():

	"""
	Solves ODE on the form:
	
	u' = f(u,t)

	with of initial condition u(t0) = U0
	"""

	def __init__(self, f):

		"""
		This class recive object 
		"""

		self.f = f

	def __str__(self):

		return f"""
			Condition initial is: {self.U0} \nTime points is: {self.N} 
			Number equations is: {self.numero_eqns_dif} 
			"""

	def condiciones_iniciales(self, U0, Deltat, dt):

		"""
		U0 is initial condition 

		U0 = [u_1, u_2, ... ,u_n]
					
		donde \"n\" es el número de ecuaciones diferenciales. 
		"""
	
		self.N = int((Deltat[1]-Deltat[0])/dt)
		self.t = np.linspace(Deltat[0], Deltat[1], self.N +1)

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

	def Solve(self):

		"""
		This function is for integration,  

		u[i + 1] = advance

		the advance is a method for solve EDO.
		"""

		self.U = np.zeros((len(self.t), (self.numero_eqns_dif)*(self.numero_coord)))

		self.U[0,:] = self.U0

		#Integration	
		for i in range(self.N):
			self.i = i 
			self.U[i + 1] = self.advance()

		return self.U, self.t


class Euler(SolveODE):
	
	"""
	Euler method is for solve equation diferential system. The Euler
	method is the form

	u[i + 1] = u[i] + f(u[i],t[i])*dt
	"""

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		return u[i, :] + dt * f(u[i, :], t[i])

class Verlet(SolveODE):

	"""
	Verlet method is for solve equation diferential. The Verlet
	method is the form
	
	u[i + 1] = 2*u[i] - u[i - 1] + f(u[i, t[i])*dt**2
	"""

	def advance(self):

		u, f, i, t = self.u, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		if self.i == 0:

			return u[i, :] + f(u[i,:], t[i])*dt 

		else:

			return 2*(self.u[i,:]) - self.u[i-1, :] + f(u[i,:] , t[i])*(dt**2)

class Runge_Kutta(SolveODE):

	pass
