/*
Caida libre (C++)

Luis Eduardo Sánchez González

Facultad de Ciencias Físico Matemáticas
Física Computacional
*/

#include<bits/stdc++.h>

using namespace std;

double Ecuacion_Dif(double y, double dy);

int main(){

	double t = 0, tf = 10, dt = 0.01;
	double l = 10, g = 9.81;

	int N = (tf-t)/dt, i = 0;

	double Posicion[N], Velocidad[N], tiempo[N];

	Posicion[0] = 1000;
	Velocidad[0] = 0;
		
	ofstream file_plot;
	file_plot.open("Solucion.txt");

	file_plot<<tiempo[i]<<"\t"<<Posicion[i]<<endl; 

	while(t < tf){

		double aceleracion = Ecuacion_Dif(Posicion[i], Velocidad[i]);

		Velocidad[i+1] = Velocidad[i] + (aceleracion)*dt;
		Posicion[i+1] = Posicion[i] + Velocidad[i+1]*dt;
		tiempo[i+1] = tiempo[i] + dt;
		
		file_plot<<tiempo[i]<<"\t"<<Posicion[i]<<endl;	

		t += dt;
		i++;

	}

	file_plot.close();

	system("python graficar.py");
			
	return 0;
}

double Ecuacion_Dif(double y, double dy){

	return -9.81;	
}
