"""
Péndulo Simple 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

def Grafica():

	plt.title("Péndulo simple")
	plt.plot(Pendulo.tiempo, Pendulo.x, label = r"$\theta (t)$")
	plt.xlabel(r"tiempo (s)")
	plt.ylabel(r"Posicion (rad)")
	plt.legend()
	plt.grid()
	plt.show()
	
def Simulacion():

	tiempo = Pendulo.tiempo

	fig = plt.figure()
	ax = fig.gca()

	def update(i):

		ax.clear()
		plt.title("Péndulo simple")
		plt.plot([0, np.sin(Pendulo.x[i])],[0,-1*np.cos(Pendulo.x[i])],"b-", color = "black")
		plt.plot(np.sin(Pendulo.x[i]), -1*np.cos(Pendulo.x[i]) ,"ro" , color = "red", label = "t = " + str(round(tiempo[i],3)) + " s")
		plt.grid()
		plt.legend()
		plt.xlim(-1,1)
		plt.ylim(-1.5,0)

	ani = animation.FuncAnimation(fig, update, range(len(tiempo)), interval = 1)
	#ani.save('Pendulo.gif', writer='imagemagick', fps=100)					#Guardar animación
	plt.show()

if __name__ == "__main__":

	import matplotlib.animation as animation
	from timeit import default_timer
	import matplotlib.pyplot as plt
	import numpy as np
	import sys

	sys.path.append("../")

	from PhyPy.PhysicalSystem import *		#Importamos la libreria que contiene los métodos

	t, tf, dt = 0, 4, 0.01
	l, g, theta_i = 1, 9.8, (10/180)*np.pi

	Aceleracion = [str(-g/l) + "*x", "0", "0"]

	posicion = np.array([0.2,0,0])
	velocidad = np.array([0,0,0])

	print("Péndulo Simple")

	Inicio = default_timer()

	Pendulo = Sistema_fisico(Aceleracion)
	Pendulo.Metodo_Euler_Cromer(t,tf,dt,posicion,velocidad)

	Final = default_timer()

	print(Pendulo)

	print("Tiempo de ejecución:", Final - Inicio)

	Grafica()
