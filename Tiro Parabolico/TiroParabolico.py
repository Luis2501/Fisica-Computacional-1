"""
Tiro parabólico (Python)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
"""

import matplotlib.pyplot as plt
from math import cos, sin, pi, sqrt
import numpy as np
import sys

sys.path.append("../")

from PhyPy.PhysicalSystem import *

def main(Rozamiento):

	t = 0 ; tf = 20 ; dt = 0.01 

	theta = (50/180)*pi ; g = 9.8 ; B = 4e-5 ; V = 70

	Vx = V*cos(theta) ; Vy = V*sin(theta)

	if Rozamiento == True:
	
		Aceleracion = [str(-B*V*Vx), str(-g) + str(-B*V*Vy), "0"]

	else:
	
		Aceleracion = ["0", str(-g), "0"]
	
	posicion = np.array([0,0,0]) ; velocidad = np.array([Vx,Vy,0])

	Tiro_Parabolico = Sistema_fisico(Aceleracion)
	Tiro_Parabolico.Metodo_Euler_Cromer(t,tf,dt,posicion,velocidad) 

	print(Tiro_Parabolico)

	plt.title("Tiro Parabolico")
	plt.plot(Tiro_Parabolico.x, Tiro_Parabolico.y)
	plt.grid()
	plt.show()

if __name__=="__main__":

	main(False)					#No rozamiento
	

