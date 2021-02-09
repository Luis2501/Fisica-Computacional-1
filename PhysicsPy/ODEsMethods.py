"""
Luis Eduardo Sánchez González

Universidad Autonoma de Coahuila
Facultad de Ciencias Físico Matemáticas

mié 03 feb 2021 13:10:46 CST 
"""
from PhysicsPy.ODEsSolver import ODESolve
import numpy as np

class Euler(ODESolve):
	
	"""
	Euler method is for solve equation diferential system. The Euler
	method is the form

	u[i + 1] = u[i] + f(u[i],t[i])*dt
	"""

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		return u[i, :] + dt * f(u[i, :], t[i])

class Euler_Cromer(ODESolve):

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		if self.numero_eqns_dif == 2:
			
			a = f(u[i,:], t[i])
			v = u[i,1] + dt*a[i,1]
			r = u[i,0] + dt*v

			return [r,v]

		else:

			raise "NotImplementedError"

class Verlet(ODESolve):

	"""
	Verlet method is for solve equation diferential. The Verlet
	method is the form
	
	u[i + 1] = 2*u[i] - u[i - 1] + f(u[i, t[i])*dt**2
	"""

	def advance(self):

		u, f, i, t = self.U, self.f, self.i, self.t
		dt = t[i + 1] - t[i]

		if self.i == 0:

			return u[i, :] + f(u[i,:], t[i])*dt 

		else:

			return 2*(u[i,:]) - u[i-1, :] + f(u[i,:] , t[i])*(dt**2)

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
