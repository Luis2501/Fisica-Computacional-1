"""
Atractor de Lorenz

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

dom 07 mar 2021 11:05:44 CST  
"""
import numpy as np

class Atractor:

	def __init__(self, rho, sigma, beta):

		self.rho, self.beta, self.sigma = rho, beta, sigma

	def __call__(self, u, t):

		x, y, z = u
		rho, beta, sigma = self.rho, self.beta, self.sigma 

		return np.array([sigma*(y-x), x*(rho - z) - y, x*y - beta*z])

if __name__=="__main__":

	
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d.axes3d import Axes3D
	import sys
	sys.path.append("../")
	from PhysicsPy.ODEsMethods import * 

	Lorenz = Atractor(rho = 28, beta = 8/3, sigma = 8)							

	Solucion = Runge_Kutta(Lorenz)						
	Solucion.InitialConditions([1,1,1], [0,25], 0.001)				
	u,t = Solucion.SolveODE()						

	plt.style.use('dark_background')

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	ax.plot(u[:,0], u[:,1], u[:,2], color="gold")	    
	plt.show()
