import numpy as np
import matplotlib.pyplot as plt

#class Orthogonal_Polinomyals:

def Hermite(x2, n):

	if n==0:

		return np.ones(len(x2))
    
	elif n==1:

		return 2*x2

	else:

		return 2*x2*Hermite(x2,n-1)-2*(n-1)*Hermite(x2,n-2)

def Legendre(x, n):

	if n == 0: 

		return np.ones(len(x))

	elif n == 1:

		return x

	else:

		return  (( x*(1+ 2*(n-1))*Legendre(x, n - 1) - (n-1)*Legendre(x, n - 2) )/(n))
	 

x = np.linspace(-1,1,1001)

for i in range(6):

	plt.plot(x, Legendre(x, i), label = f"$P_{i}$")

plt.title("Polinomios de Legendre")
plt.grid() ; plt.legend()
plt.show()
