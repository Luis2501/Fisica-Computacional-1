"""
Problema de los tres cuerpos (Sol-Tierra-Jupiter)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mié 24 mar 2021 15:29:40 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go
from Gravitation import Orbit
import numpy as np

if __name__ == "__main__":

	import sys
	sys.path.append("../") 	
	from PhysicsPy.ODEsMethods import *
	
	re, rj = 1, 5.2									#Radio de la Tierra y de Jupiter
	ve, vj = 2*np.pi, (2*np.pi*rj)/(11.86)						#Velocidad de la Tierra y Jupiter
	Ms, Mj, Me = 2e30, 1.9e27, 6e24							#Masa del Sol, Jupiter y Tierra

	fig = make_subplots(rows=2, cols=2, 
	      subplot_titles=("Mj = Mj", "Mj = 10 Mj", "Mj = 100 Mj", "Mj = 1000 Mj"))

	for i, k in zip([[1,1],[1,2],[2,1],[2,2]], [1,10,100,1000]):

		Earth_Jupiter = Orbit(Ms, k*Mj, Me, 3)					#Definimos el objeto Tierra-Jupiter
		Solution = Euler_Cromer(Earth_Jupiter, System = False)			#Instancia en la clase Euler-Cromer

		Condition = [[re, 0, rj, 0], 						#Posición (xe, ye, xj, yj)  
			     [0, ve, 0, vj]]						#Velocidad (Vxe, Vye, Vxj, Vyj)

		Time = [0, 12]								#Tiempo de 0 hasta 12 anios

		Solution.InitialConditions(Condition, Time, 0.001)			#Definimos condiciones iniciales
		u, t = Solution.SolveODE()						#Obtenemos la solución 				

		fig.add_trace(go.Scatter(x=u[:,0], y=u[:,1], name = "Tierra"), row=i[0], col=i[1])
		fig.add_trace(go.Scatter(x=u[:,2], y=u[:,3], name = "Jupiter"), row=i[0], col=i[1])

		fig.update_xaxes(title_text="x (AU)", row=i[0], col=i[1])
		fig.update_yaxes(title_text="y (AU)", row=i[0], col=i[1])

	fig.update_layout(title_text="Problema de los tres cuerpos: Sol-Tierra-Jupiter")
	fig.show()
