"""
Tiro parabólico con/sin fricción, 
incluye alcance máximo y altura máxima

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mar 23 feb 2021 09:47:28 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np

class Tiro_Parabolico:

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


	def Alcance_Maximo(self, u):

		"""
		Se busca el indice donde la posición en \"y\" es negativa, 
		de esta manera podemos saber el alcance máximo.
		"""

		for i in u[:,2]:
		
			if i < 0.0:

				return u[np.where(u[:,2] == i)[0][0] - 1, 0]

	def Altura_Maxima(self, u):

		"""
		Se busca la posición en \"y\" tal que su anterior posición es menor
		a él y su siguiente posición también lo es. Es decir, se aplica la 
		definición de máximo local.
		"""

		for i in range(len(u)):

			if u[i + 1,2] < u[i,2] and u[i-1,2] < u[i,2]:

				return u[i,2]

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import matplotlib.ticker as ticker
	from math import cos, sin, pi
	import sys
	sys.path.append("../")

	from PhysicsPy.ODEsMethods import * 

	v = 700
	Sistema = Tiro_Parabolico(v, 9.81, friccion = True, B = 4e-5)		#Instancia en la clase con fricción

	fig = plt.figure()
	ax = fig.add_subplot(111)

	print("Tiro Parabólico con fricción.\n")
	print("Para los distintos ángulos, sus alcances son: \n") 

	Alcances = []								#Arreglo para guardar los alcances

	#Tiro parabólico para distintos ángulos
	for theta in np.arange(10,100,10):
	
		Solucion = Euler(Sistema)					#Instancia para resolver con Met. Euler		

		CondInit = [0, v*cos(theta*pi/180), 0, v*sin(theta*pi/180)]

		Solucion.InitialConditions(CondInit, [0,150], 0.01)		#Definición de condiciones inciales
		u,t = Solucion.SolveODE()					#Solución numérica en forma de matriz				

		ax.plot(u[:,0], u[:,2], label=r"$\theta =$"+ f"{theta}"+"°")	#Graficamos altura vs alcance

		X_max = Sistema.Alcance_Maximo(u)				#Buscamos el alcance del movimiento
		Alcances.append([theta, X_max])					#Almacenamos el alcance y el ángulo
		
		print(f"Alcance para {theta}°: {round(X_max,4)} m" )		#Mostramos los datos

	Alcances = np.array(Alcances)

	i = (np.where(Alcances == max(Alcances[:,1])))[0][0] 			#Buscamos el alcance máximo

	print(f"\nEl alcance máximo es \"{round(Alcances[i,1], 4)} m\", cuando el ángulo es de {Alcances[i,0]}°.")
	print("\nPara saber con mayor precisión, se debe tomar un intervalo con mayor resolución de ángulos.")

	#Ajustar gráfica 
	ax.set_title("Altura vs alcance")
	ax.set_xlabel(r"$x$ (km)") ; ax.set_ylabel(r"$y$ (km)")
	ax.set_ylim(0,max(u[:,2])) 
	ax.legend() ; ax.grid()

	ticks_x = ticker.FuncFormatter(lambda y, pos: "{:.4f}".format(y/1e3))	
	ax.xaxis.set_major_formatter(ticks_x)
	ticks_y = ticker.FuncFormatter(lambda x, pos: "{:.4f}".format(x/1e3))	
	ax.yaxis.set_major_formatter(ticks_y)	

	fig.tight_layout()
	plt.show()	
