"""
Caminatas aleatorias (Multiples caminantes) 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

jue 15 abr 2021 09:55:53 CDT  

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np 

class Random_Walk:

	def __init__(self, p, N):

		if p >= 0 and p <= 1:
		
			self.p, self.N = p, N

		else: 

			raise ValueError("Probability out of range")

	def Multiple_Walkers(self, M):

		self.M = M	
		self.Steps = np.zeros((self.N, self.M)) 

		for i in range(self.M):
	
			self.Steps[:,i] = self.Walk()

		return self.Steps
					
class Random_Walk_1D(Random_Walk):	

	def Walk(self):

		N, p = self.N, self.p

		X = np.random.random(N)					
		steps = np.where((X<=p) == True, 1, -1)			 
		new_steps = np.zeros(N)					

		for i in range(len(new_steps)-1):

			new_steps[i + 1] = sum(steps[:i +1])

		return new_steps
