"""
Caida libre 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

def Visualizacion(Grafica = False, Simulacion = False):

	tiempo = Caida_Libre.tiempo

	fig = plt.figure()
	ax = fig.gca()

	def update(i):

		ax.clear()
		plt.title("Caida libre")
		plt.plot(Caida_Libre.x[i], Caida_Libre.y[i] ,"ro" , color = "blue", label = "t = " + str(round(tiempo[i],3)) + " s")
		plt.ylim(0,max(Caida_Libre.y))
		plt.legend()
		plt.grid()

	if Grafica == True:

		plt.title("Caida libre")
		plt.plot(Caida_Libre.tiempo, Caida_Libre.y, label = r"$y(t)$")
		plt.xlabel(r"tiempo (s)")
		plt.ylabel(r"Posicion (m)")
		plt.legend()
		plt.grid()

	elif Simulacion == True:

		ani = animation.FuncAnimation(fig, update, range(len(tiempo)), interval = 1)
		#ani.save('Caida_libre.gif', writer='imagemagick', fps=100)			#Guardar la simulación

	plt.show()


if __name__=="__main__":

	import matplotlib.animation as animation
	import matplotlib.pyplot as plt
	import numpy as np
	import sys

	sys.path.append("../")

	from PhyPy.PhysicalSystem import *		#Importamos la libreria que contiene los métodos

	t = 0 ; tf = 5 ; dt = 0.01 			#Definimos parámetros y condiciones inciales
	h = 100 ; g = 9.81	 			
	
	posicion = np.array([0,h,0])
	velocidad = np.array([0,0,0])

	Aceleracion = ["0", str(-g), "0"]		#Definimos la aceleración, solamente en la componente "y"				

	print("Caida libre")

	Caida_Libre = Sistema_fisico(Aceleracion)
	Caida_Libre.Metodo_Euler_Cromer(t, tf, dt, posicion, velocidad)

	print(Caida_Libre)

	Visualizacion(Grafica=True)
