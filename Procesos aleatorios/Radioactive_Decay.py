"""
Clase "Decaimiento radiactivo" 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

sáb 01 may 2021 10:12:14 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
from random import random 
import numpy as np

class Radioactive_Decay:

	def __init__(self, N0, t, p):

		self.N0, self.t, self.p = N0, t, p

	def __call__(self):

		N0, p, t = self.N0, self.p, self.t
	
		self.N = np.zeros(t)
		self.N[0] = N0
 
		for i in range(t - 1):

			for k in range(N0):

				if random() < p:

					N0 -= 1

			self.N[i + 1] = N0

		return self.N

	def decay_mean(self, M):

		try:
		
			Nt = np.zeros(self.t)
			
			for i in range(M):

				Nt += self()

			return (1/M)*Nt

		except ValueError:

			print("Decay failed")	
