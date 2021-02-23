"""
Tiro parabólico con/sin fricción

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

lun 22 feb 2021 09:15:57 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Tiro_Parabolico:

	"""
	Tiro Parabólico

	La fricción depende del parámetro "friccion", de manera
	predeterminada es sin friccion (False). 
	"""

	def __init__(self, v, g, friccion = False, B = 0):

		self.v, self.g, self.friccion, self.B = v, g, friccion, B

	def __call__(self, u, t):

		x, vx, y, vy = u 
		g, B = self.g, self.B

		if self.friccion == True:

			v = ((vx)**2 + (vy)**2)**(1/2) 	

			return np.array([vx, -B*v*vx, vy, -g - B*v*vy])

		else:

			return np.array([vx, 0, vy, -g]) 


if __name__=="__main__":

	import matplotlib.pyplot as plt
	import matplotlib.ticker as ticker
	from math import cos, sin, pi
	import sys
	sys.path.append("../")

	from PhysicsPy.ODEsMethods import * 

	v = 700
	Sistema = Tiro_Parabolico(v, 9.81, friccion = True, B = 4e-5)		#Instancia en la clase

	fig, (ax1,ax2) = plt.subplots(1, 2, figsize = (13,13))

	#Tiro parabólico para distintos ángulos
	for theta in range(10,100,10):
	
		Solucion = Euler(Sistema)					#Instancia para resolver con Met. Euler

		CondInit = [0, v*cos(theta*pi/180), 0, v*sin(theta*pi/180)]

		Solucion.InitialConditions(CondInit, [0,120], 0.01)		#Definición de condiciones inciales
		u,t = Solucion.SolveODE()					#Solución numérica en forma de matriz

		#Gráfica altura vs alcance
		ax1.set_title("Altura vs alcance")
		ax1.plot(u[:,0], u[:,2], label = r"$\theta =$" + f"{theta}" + "°")
		ax1.set_xlabel(r"$x$ (km)") ; ax1.set_ylabel(r"$y$ (km)")
		ax1.set_ylim(0,max(u[:,2])) 
		ax1.legend() ; ax1.grid()

		V = ((u[:,1])**2 + (u[:,3])**2)**(1/2) 				#Magnitud de la velocidad del objeto
		
		#Gráfica velocidad vs tiempo
		ax2.set_title("Velocidad vs tiempo")
		ax2.plot(t, V, label = r"$\theta =$" + f"{theta}" + "°")
		ax2.set_xlabel("tiempo (s)") ; ax2.set_ylabel("Velocidad (m/s)")
		ax2.set_xlim(0,max(t))
		ax2.legend() ; ax2.grid()

	#Ajustar los ejes 
	ticks_x = ticker.FuncFormatter(lambda y, pos: "{:.1f}".format(y/1e3))	
	ax1.xaxis.set_major_formatter(ticks_x)
	ticks_y = ticker.FuncFormatter(lambda x, pos: "{:.1f}".format(x/1e3))	
	ax1.yaxis.set_major_formatter(ticks_y)	
	
	print(u)

	fig.tight_layout()
	plt.show()	
