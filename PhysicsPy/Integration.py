import numpy as np

class Integration:

	def __init__(self, f):

		self.f = f

	def Limits(self, a, b, dx):

		self.a, self.b, self.dx = a, b, dx

		if a > b:

			raise ValueError("Wrong limits, a > b")

		if a == b:

			raise ValueError("Wrong limits, a = b \n ∫ f(x) dx = 0")

		self.N = int((b-a)/dx)
	

	def Solve(self):

		self.x = np.linspace(self.a, self.b, self.N + 1)
		self.S = np.zeros(self.N)

		self.S[0] = self.f(self.a)*self.dx

		for i in range(1, self.N):

			self.i = i

			self.S[i] = self.advance()

		return sum(self.S)


class Riemann(Integration):

	def advance(self):
					
		f, x, i = self.f, self.x, self.i		
		dx = x[i +1] - x[i]

		return f(x[i +1])*dx
						

class Monte_Carlo:

	def advance(self):

		pass


def f(x):
	return 2*x

Integral = Riemann(f)

Integral.Limits(1,0,0.0001)
print(Integral.Solve())

			
