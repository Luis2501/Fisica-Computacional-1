program CaidaLibre
implicit none

real :: t, tf, dt, y, dy, f
integer :: n, i 
real, dimension(:), allocatable :: Posicion, Velocidad, tiempo

t = 0 ; tf = 5 ; dt = 0.01

n = (tf - t)/dt

ALLOCATE(Posicion(n), Velocidad(n), tiempo(n))

Posicion(1) = 100
Velocidad(1) = 0
tiempo(1) = 0

 open(10, file ="Solucion_Fortran.dat")

	i = 1

	write(10,*) tiempo(i), Posicion(i), Velocidad(i)

	do while(t.le.tf)

		Velocidad(i+1) = Velocidad(i) + (f(Posicion(i), Velocidad(i)))*dt

		Posicion(i+1) = Posicion(i) + Velocidad(i+1)*dt;

		tiempo(i+1) = tiempo(i) + dt;
		
		write(10,*) tiempo(i), Posicion(i), Velocidad(i)	

		t = t + dt;
		i = i + 1

	enddo

 close(10)	

call system("gnuplot -p Grafica_Fortran.gp")

end program

real function f(y,dy)

	real :: y,dy

	f =  -9.81

end function
