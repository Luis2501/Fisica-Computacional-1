"""
Caida libre (Python)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

if __name__=="__main__":

	import matplotlib.pyplot as plt
	import numpy as np
	import sys

	sys.path.append("../")

	from PhyPy.PhysicalSystem import *		#Importamos la libreria que contiene los métodos

	t = 0 ; tf = 5 ; dt = 0.01 			#Definimos parámetros y condiciones inciales
	h = 100 ; g = 9.81	 			
	
	posicion = np.array([0,h,0])
	velocidad = np.array([0,0,0])

	Aceleracion = ["0", str(-g), "0"]		#Definimos la aceleración, solamente actua en la componente "y"				

	Caida_Libre = Sistema_fisico(Aceleracion)
	Caida_Libre.Metodo_Euler_Cromer(t, tf, dt, posicion, velocidad)

	plt.title("Caida libre")
	plt.plot(Caida_Libre.tiempo, Caida_Libre.y, label = r"$y(t)$")
	plt.xlabel(r"tiempo (s)")
	plt.ylabel(r"Posicion (m)")
	plt.legend()
	plt.grid()
	plt.show()
