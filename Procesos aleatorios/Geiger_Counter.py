"""
Contador Geiger-Müller 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

sáb 01 may 2021 10:12:14 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
import numpy as np
from time import sleep
from random import random
from tkinter import *
import threading
import matplotlib.pyplot as plt

class UI(Frame):
  
	def __init__(self, parent=None, N0=1000, t=100, p=0.01):

		Frame.__init__(self, parent)
		
		self.N0, self.t, self.p = N0, t, p
	
		self.parent = parent
		self.init_ui()
	
	def init_ui(self):
    
		self.parent.title("Geiger-Müller Counter")

		self.N = StringVar()
		self.N.set(self.N0)
		
		self.parent.label = Label(font=("Verdana",24))
		self.parent.label.pack(padx = 50, pady = 20)
		self.parent.label.config(textvariable=self.N)
	
		self.parent.iniciar = Button(text = "Iniciar", command = self.Decay)
		self.parent.iniciar.pack(pady = 20)

		self.hilo = threading.Thread(target=Decay)
	
	def Decay(self):
		
		N0, p, t = self.N0, self.p, self.t
 
		for i in range(t - 1):

			for k in range(N0):

				if random() < p:

					N0 -= 1
					self.N.set(N0)
					sleep(4)
					self.Beep()

	def Beep(self):

		print("\a")

if __name__ == "__main__":

	root = Tk()

	app = UI(parent=root, N0=10000, t=100, p=0.01)	
	app.mainloop()
	
