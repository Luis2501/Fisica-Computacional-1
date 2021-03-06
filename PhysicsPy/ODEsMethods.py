"""
Luis Eduardo Sánchez González

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas

mié 03 feb 2021 13:10:46 CST 
"""
from PhysicsPy.ODEsSolver import ODESolve
import numpy as np

class Euler(ODESolve):

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		return u[i, :] + dt * f(u[i, :], t[i])

class Euler_Cromer(ODESolve):

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt, k = t[i + 1] - t[i], self.NumCoor

		if k == 1:

			x2 = u[i,1] + dt*(f(u[i, :], t[i])[1])
			x1 = u[i,0] + dt*x2

			return np.array([x1,x2])

		else: 

			x2 = u[i,k:] + dt*(f(u[i, :], t[i])[k:]) 
			x1 = u[i,:k] + dt*x2
		
			return np.concatenate((x1, x2))

class Runge_Kutta(ODESolve):

	def advance(self):

	        u, f, i, t = self.U, self.f, self.i, self.t
	        dt = t[i + 1] - t[i]
	        dt2 = dt / 2
        	K1 = dt * f(u[i, :], t[i])
        	K2 = dt * f(u[i, :] + 0.5 * K1, t[i] + dt2)
        	K3 = dt * f(u[i, :] + 0.5 * K2, t[i] + dt2)
        	K4 = dt * f(u[i, :] + K3, t[i] + dt)

	        return u[i, :] + (1 / 6) * (K1 + 2 * K2 + 2 * K3 + K4)

class Verlet(ODESolve):

	"""
	Solucionar bien
	"""

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		if i == 0: 

			return u[i, :] + dt * f(u[i, :], t[i])

		else: 

			return 2*u[i,:] - u[i-1,:] + f(u[i, :], t[i])*(dt**2)		

