"""
Decaimiento radiactivo 3

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

lun 03 may 2021 17:44:15 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
from Radioactive_Decay import Radioactive_Decay
import matplotlib.pyplot as plt
import numpy as np

Nucleos = Radioactive_Decay(10000, 100, 0.01)					#Creamos el objeto con las propiedades N0 = 10,000, p = 0.01
	
t, N = np.linspace(0,99,100), Nucleos.decay_mean(100)				#Obtenemos el tiempo y la media, después de hacer 100 experimentos

λ, N0  = np.polyfit(t, np.log(N), 1)						#Ajuste de los datos, se obtiene N0 y λ 		

N_t = np.exp(N0)*np.exp(λ*t)							#Función N(t) = N0*exp(-λt)  

print("\nAjuste de la curva \n")
print(f"N(t) = ({round(np.exp(N0), 6)})*exp({round(λ, 6)}*t) ")			#Imprimir el ajuste
print(f"\nPor lo tanto,\n\nλ = {round(λ, 6)} \n")				#Imprimir el valor de λ

plt.style.use("seaborn")	
plt.title("Decaimiento radioactivo")
plt.plot(t, N, color = "orange", label = r"$\langle N(t) \rangle$")		#Gráficamos <N(t)> 
plt.plot(t, N_t, color = "blue", label = r"Fit $\langle N(t) \rangle$")		#Gráficamos Fit <N(t)> 
plt.xlabel(r"Tiempo (s)")  ; plt.ylabel(r"Número de núcleos (N)")
plt.legend(fancybox = True) ; plt.grid(True) 

plt.show()
