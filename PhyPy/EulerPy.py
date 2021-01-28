"""
Luis Eduardo Sánchez González

Miercoles 2 de diciembre de 2020
"""

class Euler():

	def Metodo_Euler(self, t, tf, dt, posicion):
	
		self.Posicion.append(posicion)
		self.tiempo.append(t)

		while t <= tf:

			velocidad = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad[0],
					                       y = posicion[1], dy = velocidad[1], 
				                               z = posicion[2], dz = velocidad[2]) 

			posicion = posicion + (velocidad)*dt
			self.Posicion.append(posicion)

			t += dt
			self.tiempo.append(t)

		R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]	
	
		return R(0), R(1), R(2)

	def Metodo_Euler_Cromer(self, t, tf, dt, posicion, velocidad): 

		self.tiempo.append(t)
		self.Posicion.append(posicion)
		self.Velocidad.append(velocidad)

		while t <= tf:

			aceleracion = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad[0],
					                         y = posicion[1], dy = velocidad[1], 
					                         z = posicion[2], dz = velocidad[2]) 

			velocidad = velocidad + (aceleracion)*dt			
			posicion = posicion + (velocidad)*dt
			
			self.Posicion.append(posicion)
			self.Velocidad.append(velocidad)

			t += dt
			self.tiempo.append(t)
			
			

		R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]
		V = lambda m: [self.Velocidad[i][m] for i in range(len(self.Velocidad))]

		self.x = R(0); self.y = R(1); self.z = R(2)
		self.V_x = V(0); self.V_y = V(1); self.V_z = V(2)

