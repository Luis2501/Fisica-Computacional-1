"""
Métodos Variacionales: App Principio de Fermat

NOTA: Se hicieron correciones en el método

Para ejecutar:

	python App_Fermat.py 

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional

jue 13 may 2021 13:08:29 CDT 

Repositorio: https://github.com/Luis2501/Fisica-Computacional-1
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Fermat_Class import Fermat
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np

class UI(Frame):
  
	def __init__(self, parent=None, M=15000, N=6, si=(0,0), sf=(2,1)):
	
		"""Initialize the window"""

		Frame.__init__(self, parent)
	
		self.parent = parent
		
		self.M, self.N = M, N
		self.si, self.sf = si, sf
		
		self.init_ui()
	
	def init_ui(self):
	
		"""Create objects in the window"""
    
		self.parent.title("App Fermat's Principle")
		self.parent.geometry("700x600")
	
		self.instance_Fermat()
		self.bar_menu()
		
	def instance_Fermat(self):
	
		"""Generates a first trajectory and draws it"""
	
		self.rayo = Fermat([1, 1.5])
		self.rayo.set_conditions(si=self.si, sf=self.sf, N=self.N)
		self.xi, self.yi = self.rayo.x, self.rayo.y_init
		
		self.init_graph()
		
	def clean(self):
	
		"""Clean the graph"""
	
		self.parent.geometry("700x600")
		self.ax.clear()
	
		self.ax.grid(True)
		self.ax.set_xlabel(r"$x$") 
		self.ax.set_xlabel(r"$y$")
		self.ax.set_xlim(self.rayo.xi, self.rayo.xf)
		self.ax.set_ylim(self.rayo.yi, self.rayo.yf)
		self.ax.axvline(self.rayo.xf/2, self.rayo.yi, self.rayo.yf, linestyle=":")
		self.canvas.draw()	
		
	def start(self):
	
		"""Take M steps and draw them"""
	
		self.instance_Fermat()
	
		for i in range(self.M):
	
			self.rayo.advance() 
			
			if self.rayo.Change:
			
				self.clean()
				self.ax.plot(self.rayo.x, self.rayo.y, label=f"{i+1}")
				self.ax.legend() ; self.canvas.draw()
		
		self.xf, self.yf = self.rayo.x, self.rayo.y,	
		self.ax.plot(self.xf, self.yf, label = "Final trajectory")
		
		self.canvas.draw()
		
	def result(self):
	
		"""Show the results of Snell's law"""
	
		self.windowResult = Toplevel(self.parent)	
		self.windowResult.title("Snell's Law")

		self.fig1 = plt.Figure(figsize=(5, 4), dpi=100)
		self.ax1 = self.fig1.add_subplot(111)

		self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.windowResult)
		self.canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		self.canvas1._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

		self.ax1.get_xaxis().set_visible(False)
		self.ax1.get_yaxis().set_visible(False)

		n1, n2 = self.rayo.snell_law()

		self.ax1.clear()
		self.ax1.text(0.3, 0.9, r"Snell's Law", fontsize = 15)
		self.ax1.text(0.2, 0.8, r"$n_1 sin(\theta_1) = n_2 sin(\theta_2)$", fontsize = 15)
		self.ax1.text(0.01, 0.6, r"Approximation results: ", fontsize = 15)
		self.ax1.text(0.01, 0.4, fr"$n_1 sin(\theta_1) = {n1}$", fontsize = 15)	  
		self.ax1.text(0.01, 0.3, fr"$n_2 sin(\theta_2) = {n2}$", fontsize = 15)
		self.ax1.text(0.01, 0.1, f"Absolute error: {abs(n1-n2)}", fontsize = 15)
		self.ax1.text(0.01, 0.01, f"Relative error: {abs(n1-n2)/n1}", fontsize = 15)		
		self.canvas1.draw()

	def final_graph(self):
	
		"""Shows the final graph with initial and final trajectory"""
	
		self.clean()
		self.ax.plot(self.xi, self.yi, label="Initial trajectory")
		self.ax.plot(self.xf, self.yf, label = "Final trajectory")
		self.ax.set_title("Fermat's Principle")
		self.ax.legend()
		self.canvas.draw()

	def init_graph(self):
	
		"""Initialize the graph in the window"""
	
		plt.style.use("seaborn")
		self.fig = plt.Figure()
		self.ax = self.fig.gca()
			 
		self.ax.set_xlabel(r"$x$") ; self.ax.set_xlabel(r"$y$")
		self.ax.set_xlim(self.rayo.xi, self.rayo.xf)
		self.ax.set_ylim(self.rayo.yi, self.rayo.yf)
		self.ax.plot(self.rayo.x, self.rayo.y_init, label="Initial trajectory")
		self.ax.axvline(self.rayo.xf/2, self.rayo.yi, self.rayo.yf, linestyle=":")
		self.ax.grid(True) ; self.ax.legend()
		
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent) 
		self.canvas.get_tk_widget().place(x=0, y=0, width=700, height=600)
		self.canvas.draw()

	def bar_menu(self):

		"""Create the menu bar"""
	
		self.menubarra = Menu(self.parent)

		self.menubarra.add_command(label = "Start", command = self.start)
		self.menubarra.add_command(label = "Clean", command = self.clean)
		self.menubarra.add_command(label = "Snell's Law", command= self.result)
		self.menubarra.add_command(label = "Final Graph", command= self.final_graph)
		self.menubarra.add_command(label = "Exit", command= self.parent.quit)

		self.parent.config(menu=self.menubarra)

if __name__ == "__main__":

	"""
	The initial conditions are:
		
		Initial position: (0,0) 
		Final position: (2,1)
		Number of intermediate points: 6
		Number of steps: 15,000
	"""

	root = Tk()
	
	app = UI(parent=root)	
		
	app.mainloop()	
