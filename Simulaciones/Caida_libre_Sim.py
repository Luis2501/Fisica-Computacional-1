"""
Simulación de caida libre

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

if __name__=="__main__":

	import matplotlib.animation as animation
	import matplotlib.pyplot as plt
	import numpy as np
	import sys

	sys.path.append("../")

	from PhyPy.PhysicalSystem import *		#Importamos la libreria que contiene los métodos

	t = 0 ; tf = 4.5 ; dt = 0.01 			#Definimos parámetros y condiciones inciales
	h = 100 ; g = 9.81	 			
	
	posicion = np.array([0,h,0])
	velocidad = np.array([0,0,0])

	Aceleracion = ["0", str(-g), "0"]		#Definimos la aceleración, solamente actua en la componente "y"				

	Caida_Libre = Sistema_fisico(Aceleracion)
	Caida_Libre.Metodo_Euler_Cromer(t, tf, dt, posicion, velocidad)

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
		

	ani = animation.FuncAnimation(fig, update, range(len(tiempo)), interval = 1)

	ani.save('Caida_libre.gif', writer='imagemagick', fps=100)

	plt.show()
