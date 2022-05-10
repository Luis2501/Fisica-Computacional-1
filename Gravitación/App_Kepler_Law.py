"""
Movimiento planetario (Modelo 3D Tercera ley de Kepler) 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

jue 18 mar 2021 09:05:20 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import plotly.graph_objects as go
import numpy as np
import sys
sys.path.append("../") 
from PhysicsPy.ODEsMethods import *
from Kepler_Law import Orbit

global Data 

Data = []

def Get_Orbit(planet, r, T): 

	global Data

	Planet = Orbit(planet, r)						
	Solution = Euler_Cromer(Planet, System = False)				

	Condition = [[r,       0], 						
	     	     [0, (2*np.pi*r)/T]]	
				
	Time = [0, T]								

	Solution.InitialConditions(Condition, Time, 0.001)			
	u, t = Solution.SolveODE()						

	z = np.zeros(len(u[:,0]))

	trace = go.Scatter3d(x=u[:,0], y=u[:,1], z=z, marker=dict(size=0.1), 
			     name = planet, line=dict(color="white", width=2))

	Data.append(trace)

def Create_Planet(Diameter, color, r, name): 
   
	theta = np.linspace(0,2*np.pi,100)
	phi = np.linspace(0,np.pi,100)
    
	x = r + Diameter*np.outer(np.cos(theta), np.sin(phi))
	y = Diameter*np.outer(np.sin(theta), np.sin(phi))
	z = Diameter*np.outer(np.ones(100), np.cos(phi))
    
	trace= go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], name = name)
	trace.update(showscale=False)

	return trace

if __name__ == "__main__":

	#Diccionario, información de los planetas
	Solar_System = {"Planets" : ["Sun", "Venus", "Earth", "Mars", "Jupyter", "Saturn"], 
		      	"Radius" : [0, 0.72, 1, 1.52, 5.2, 9.54], 
		      	"Diameter" : [0.134,  8.1e-3, 8.1e-3, 4.5e-3, 0.095, 0.08], 
		      	"Period" : [0, 0.61, 1, 1.88, 11.86, 29.47], 
		      	"Colors": ["#ffff00", "#d23100", "#325bff", "#b20000", "#ebebd2", "#ebcd82"] } 		

	#Creamos el Sol
	Data.append(Create_Planet(Solar_System["Diameter"][0], Solar_System["Colors"][0], 
				  Solar_System["Radius"][0], Solar_System["Planets"][0] ))

	#Creamos las órbitas y los planetas
	for i in range(1, 6): 

		trace = Create_Planet(Solar_System["Diameter"][i], Solar_System["Colors"][i], 
				      Solar_System["Radius"][i], Solar_System["Planets"][i] )

		Get_Orbit(Solar_System["Planets"][i], Solar_System["Radius"][i], Solar_System["Period"][i])

		Data.append(trace)
	
	theta = np.linspace(-2*np.pi, 2*np.pi, 1001)

	#Generar anillos de Saturno 
	for r in np.arange(0.095, 0.15, 0.01):

		x = Solar_System["Radius"][5] + r*np.cos(theta)
		y = r*np.sin(theta)
		z = np.zeros(len(x))	
		
		Data.append(go.Scatter3d(x=x, y=y, z=z, marker=dict(size=0.1), line=dict(color='#827962',width=3)))

	layout=go.Layout(title = "Solar System", showlegend=False, margin=dict(l=0, r=0, t=0, b=0),
			 scene = dict(xaxis=dict(title='x (AU)', titlefont_color="black", 
                                                 range=[-10,10], backgroundcolor='black',
                                                 color='black', gridcolor='black'),
                                      yaxis=dict(title='y (AU)', titlefont_color='black',
                                                 range=[-10,10], backgroundcolor='black',
                                                 color='black', gridcolor='black'),
                                      zaxis=dict(title='',  range=[-10,10],
                                                 backgroundcolor='black',
                                                 color='white',  gridcolor='black') ) )

	fig = go.Figure(data = Data, layout = layout)
	fig.show()	
