from math import log10
import numpy as np 

class EquationsSolver:

	def __init__(self, f, df = None):

		self.f, self.df = f, df

	def InitialCondition(self, x0, tol, maxiter = None):

		if isinstance(x0, (int, float)):
	
			self.point, self.interval = True, False
			x0 = float(x0)

		else:

			self.point, self.interval = False, True
			x0 = list(x0)

		self.x0, self.tol, self.maxiter = x0, tol, maxiter

class Biseccion(EquationsSolver):

	def Solve(self):

		if isinstance(self.x0, (int, float)):
	
			raise ValueError("No se definió un intervalo")

		a, b  = self.x0 
		f, tol = self.f, self.tol
		
		if a > b:

        		raise ValueError("Intervalo mal definido")

		if f(a) * f(b) >= 0.0:
        
			raise ValueError("La función debe cambiar de signo en el intervalo")

		if tol <= 0:

        		raise ValueError("La cota de error debe ser un número positivo")
		
		x = (a + b) / 2.0

		while True:

			if b - a < tol:

				#return round(x, int(abs(log10(tol)))
				return x
      
			elif np.sign(f(a)) * np.sign(f(x)) > 0:
	
            			a = x

			else:
				b = x
			
			x = (a + b) / 2.0

class Newton_Rhapson(EquationsSolver):

	def Solve(self):
   
		x, f, df, maxiter, tol = self.x0, self.f, self.df, self.maxiter, self.tol 
	
		if df(x) == 0:

			raise ValueError("Division por cero")
    		
		for i in range(maxiter):

		        dx = -f(x) / df(x) 

		        x = x + dx

		        if abs(dx / x) < tol and abs(f(x)) < tol:

		            return x

		raise RuntimeError(f"No hubo convergencia después de {maxiter} iteraciones")

def f(x):

	return x**3 - 5

def df(x):

	return 3*x**2 

if __name__ == "__main__":

	Solucion = Biseccion(f)
	Solucion.InitialCondition([0, 3], 1e-6)
	x = Solucion.Solve()
	
	Solucion1 = Newton_Rhapson(f, df)
	Solucion1.InitialCondition(3, 1e-6, maxiter = 1000)
	x1 = Solucion1.Solve()
	
	print(x, x1)
