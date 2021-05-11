"""
Monte Carlo, áres y π

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mar 11 may 2021 09:15:56 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import matplotlib.pyplot as plt
import numpy as np 

N = 1000000

x = np.random.random(N)
y = np.random.random(N)

θ = np.linspace(0, np.pi/2, 1001)

Num_In = len(np.where(y <= np.sqrt(1 - x**2))[0])
In = np.where(y < np.sqrt(1 - x**2), y, None) 
			
Out = np.where(y >= np.sqrt(1 - x**2), y, None)			

print("\nMétodo de Monte Carlo: Cálculo de π\n")
print("Número de puntos: ", N, "\n")
print("Área aproximada:", (Num_In)/N, "\n")
print("Aproximación de π:", round((4*Num_In)/N, 5), "\n")

plt.style.use("seaborn")
plt.title(r"Método de Monte Carlo: Cálculo de $\pi$")
plt.scatter(x, In, marker="o", color="orange", label = "Points in")
plt.scatter(x, Out, marker="o", color="blue", label = "Points out")
plt.plot(np.cos(θ), np.sin(θ), color="red", label = r"$x^2 + y^2 = 1$")
plt.legend(loc="lower right", ncol=3, mode="expand",shadow=False,fancybox=True)
plt.ylim(-0.15, 1) ; plt.grid(True) ; plt.show()
