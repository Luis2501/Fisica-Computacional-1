"""
Circuito RC (App) *Requiere libreria Plotly*

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional 

mié 10 mar 2021 09:12:48 CST 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import plotly.graph_objects as go
from Circuito_RC import RC_Circuit, SolveCircuit					#Módulo que soluciona el circuito
import numpy as np

f = np.asarray([10, 50, 100, 160, 200, 500, 1000, 5000, 10000])				#Frecuencias a utilizar en la fuente de voltaje
T = 1/f											#Periodo de oscilación

R, C = 1e3, 1e-6									#Valores de resistencia y capacitancia

QQ, tt, VVs = SolveCircuit(f, T, R, C)							#Obtener la solución para las distintas frecuencias

#Creamos figura con deslizador, nos permitirá visualizar 
#la solución para distintas frecuencias

fig = go.Figure()

for i in range(9):
    
    fig.add_trace(go.Scatter(visible=False, name ="$V_C$", x=tt[i], y=QQ[i]/C))
    fig.add_trace(go.Scatter(visible=False, name ="$V_S$", x=tt[i], y=VVs[i]))
    fig.add_trace(go.Scatter(visible=False, name ="$V_R$", x=tt[i], y=VVs[i] - QQ[i]/C))

for i in range(3):

    fig.data[i].visible = True 

steps = []										#Lista que contendra los distintos frames

for i, ff in zip(range(0, len(fig.data), 3), f):

    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Frecuencia: " + str(ff) + " Hz"}],  
    )

    step["args"][0]["visible"][i:i+2] = [True for i in range(3)]   
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frecuencia: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(sliders=sliders)
fig.update_layout(title="Circuito RC", xaxis_title="tiempo (s)", yaxis_title ="Voltaje (V)")

fig.show()
