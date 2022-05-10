"""
Métodos Variacionales: Clase Principio de Fermat

NOTA: Se hicieron correciones en el método

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

jue 13 may 2021 13:08:29 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
from random import randint, random
import numpy as np 

class Fermat:

	def __init__(self, n):

		self.Index = np.array(n)

	def set_conditions(self, si, sf, N):

		self.xi, self.yi = si	
		self.xf, self.yf = sf				

		self.N = N

		self.x = np.linspace(self.xi, self.xf, self.N+1)
			
		self.y = self.yi + (self.yf-self.yi)*np.random.random(self.N+1)
					
		self.y[0], self.y[-1] = self.yi,self.yf		

		self.y_init = self.y.copy()

		self.n = np.zeros(self.N)

		for i in range(self.N):
			
			if i < self.N/len(self.Index) :
			
				self.n[i] = self.Index[0]
						
			else: 
				
				self.n[i] = self.Index[1]

		self.Change = False	

	def advance(self):

		N, n = self.N, self.n
		y, x = self.y, self.x

		self.Change = False
		
		i = randint(1, self.N-1)

		new_y = y[i] + (0.1)*(-1 + 2*random())

		LCO = np.sqrt((self.y[i]- self.y[i-1])**2 + (x[i] - x[i-1])**2)*n[i-1] 
		LCO += np.sqrt((self.y[i]- self.y[i+1])**2 + (x[i] - x[i+1])**2)*n[i]
				
		new_LCO = np.sqrt((new_y - self.y[i-1])**2 + (x[i] - x[i-1])**2)*n[i-1] 
		new_LCO += np.sqrt((new_y - self.y[i+1])**2 + (x[i] - x[i+1])**2)*n[i]
		
		if new_LCO < LCO:

			self.y[i] = new_y
			self.Change = True
			
	def snell_law(self):
	
		N, n = self.N, self.n
		y, x = self.y, self.x
		
		i = int(N/2) 
		
		h1 = np.sqrt((y[i]- y[0])**2 + (x[i] - x[0])**2)
		h2 = np.sqrt((y[i]- y[-1])**2 + (x[i] - x[-1])**2)
		
		n1 = n[0]*((y[i] - y[0])/h1)
		n2 = n[-1]*((y[-1]- y[i])/h2)
	
		return n1, n2
