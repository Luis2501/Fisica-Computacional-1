"""
Luis Eduardo Sánchez González

Miercoles 2 de diciembre de 2020
"""

class Runge_Kutta():

		def Metodo_Runge_Kutta(self, t, tf, dt, posicion):

			self.tiempo.append(t)
			self.Posicion.append(posicion)
		
			while t <= tf:
		
				K1 = self.Ec_Diferencial(t = t, x = posicion[0],
							        y = posicion[1],
							        z = posicion[2])

				K2 = self.Ec_Diferencial(t = t + dt/2, x = posicion[0] + K1[0]*dt/2,
							               y = posicion[1] + K1[1]*dt/2,
							               z = posicion[2] + K1[2]*dt/2)

				K3 = self.Ec_Diferencial(t = t + dt/2, x = posicion[0] + K2[0]*dt/2,
							               y = posicion[0] + K2[1]*dt/2,
							               z = posicion[0] + K2[2]*dt/2)

				K4 = self.Ec_Diferencial(t = t + dt, x = posicion[0] + K3[0]*dt, 
						     	             y = posicion[1] + K3[1]*dt,
							             z = posicion[2] + K3[2]*dt)
				
				posicion = posicion + (dt/6)*(K1 + 2*K2 + 2*K3 + K4)

				self.Posicion.append(posicion)
				t += dt
				self.tiempo.append(t)

			R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]
	
			self.x = R(0); self.y = R(1); self.z = R(2)

#-------------------------------------------------------------------------------------------------

		def Metodo_Runge_Kutta_2(self, t, tf, dt, posicion, velocidad):

			self.tiempo.append(t)
			self.Posicion.append(posicion)
			self.Velocidad.append(velocidad)

			while t <= tf:

				K1 = velocidad*dt

				K2 = self.Ec_Diferencial(t = t, x = posicion[0], dx = velocidad[0],
					                	y = posicion[1], dy = velocidad[1], 
					                	z = posicion[2], dz = velocidad[2])*dt 
			
				K3 = (velocidad + K2/2)*dt
			
				K4 = self.Ec_Diferencial(t = t + dt/2, x = posicion[0] + K1[0]/2, dx = velocidad[0],
					                       	       y = posicion[1] + K1[1]/2, dy = velocidad[1], 
					                       	       z = posicion[2] + K1[2]/2, dz = velocidad[2])*dt 
	
				posicion = posicion + K3
				velocidad = velocidad + K4

				self.Posicion.append(posicion)
				self.Velocidad.append(velocidad)

				t += dt
				self.tiempo.append(t)

			R = lambda m: [self.Posicion[i][m] for i in range(len(self.Posicion))]
			V = lambda m: [self.Velocidad[i][m] for i in range(len(self.Velocidad))]

			self.x = R(0); self.y = R(1); self.z = R(2)
			self.V_x = V(0); self.V_y = V(1); self.V_z = V(2)


