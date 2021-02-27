import matplotlib.pyplot as plt
import numpy as np

print("Graficación en matplotlib")

t,x = np.loadtxt("Solucion.txt", skiprows=0, unpack=True)

plt.plot(t,x)
plt.grid()
plt.show()
