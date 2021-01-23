import matplotlib.pyplot as plt
from FisicaCompuPy.SistemaFisico import *
import numpy as np
from timeit import default_timer

dt = 0.1
t = 0
tf = 10

m = 1
k = 1

Aceleracion = [str(-k/m) + "*x", "0", "0"]

posicion = np.array([1,0,0])
velocidad = np.array([0,0,0])

starttime = default_timer()

Oscilador = Sistema_fisico(Aceleracion)
Oscilador.Metodo_Euler_Cromer(t,tf,dt,posicion,velocidad) 
plt.plot(Oscilador.tiempo, Oscilador.x, label = "Euler")

print("Euler Cromer:", default_timer() - starttime)

print(Oscilador)

plt.title("Oscilador armónico")
plt.grid()
plt.legend()
plt.show()
