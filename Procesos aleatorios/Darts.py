"""
Distribución de Poisson

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

mié 28 abr 2021 17:55:14 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np
from math import factorial

def Poisson(M, N, E):

	x = np.random.randint(1, M + 1, size=(N, E))

	Celda, Num_dardos = np.unique(x, return_counts=True)

	n, Hn = np.unique(Num_dardos, return_counts=True)

	Pn = Hn/M
	
	l, P = np.mean(n), np.zeros(len(n))

	for i in range(len(n)):

		P[i] = ((l**(n[i]))/factorial(int(n[i])))*np.exp(-l)

	return n, Pn, P
	
if __name__ == "__main__":

	import matplotlib.pyplot as plt

	n, Pn, P = Poisson(500, 50, 100)

	Eq, cl = ["Experimental", "Poisson"], ["blue", "orange"]

	fig, (ax1,ax2) = plt.subplots(1, 2, figsize = (9,4.5))

	for ax, PP, lb, c in zip([ax1, ax2], [Pn, P], Eq, cl):

		ax.set_title("Distribución de Poisson")
		ax.bar(n, PP, color = c, label = lb)
		ax.set_xlabel("n") ; ax.set_ylabel("P(n)")
		ax.legend(fancybox =True) ; ax.grid(ls='--', alpha=0.5)	

	fig.tight_layout()
	plt.show()
