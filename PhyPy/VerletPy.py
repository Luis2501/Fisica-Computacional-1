"""
Luis Eduardo Sánchez González

Miercoles 2 de diciembre de 2020
"""

class Verlet():

	def Metodo_Verlet(self, t, tf, dt, posicion, velocidad):
		
		self.tiempo.append(t)
		self.Posicion.append(posicion)

		i = 0

		while self.tiempo[-1] <= tf:

			aceleracion = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad[0], 
						                 y = posicion[1], dy = velocidad[1], 
					                         z = posicion[2], dz = velocidad[2])

			if i == 0:

				velocidad = velocidad + aceleracion*dt
				posicion = posicion + velocidad*dt 

			else:

				posicion = 2*(self.Posicion[i]) - self.Posicion[i-1] + (aceleracion)*(dt**2)
			
			self.Posicion.append(posicion)
			self.tiempo.append(self.tiempo[i] + dt)
			i+=1

		R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]

		self.x = R(0); self.y = R(1); self.z = R(2)

#-----------------------------------------------------------------------------------------

	def Metodo_Velocity_Verlet(self, t, tf, dt, posicion, velocidad):

		self.tiempo.append(t)
		self.Posicion.append(posicion)
		self.Velocidad.append(velocidad)

		while t <= tf:

			aceleracion = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad[0], 
						                 y = posicion[1], dy = velocidad[1], 
					                         z = posicion[2], dz = velocidad[2])

			posicion = posicion + velocidad*dt + (1/2)*(aceleracion)*(dt**2)

			velocidad_1 = velocidad + (aceleracion)*dt

			aceleracion_1 = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad_1[0], 
						                   y = posicion[1], dy = velocidad_1[1], 
					                           z = posicion[2], dz = velocidad_1[2])
  
			velocidad = velocidad + dt*(aceleracion + aceleracion)/(2) 

			self.Posicion.append(posicion)
			self.Velocidad.append(velocidad)

			t += dt
			self.tiempo.append(t)

		R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]
		V = lambda m: [self.Velocidad[i][m] for i in range(len(self.Velocidad))]

		self.x = R(0); self.y = R(1); self.z = R(2)
		self.V_x = V(0); self.V_y = V(1); self.V_z = V(2)
