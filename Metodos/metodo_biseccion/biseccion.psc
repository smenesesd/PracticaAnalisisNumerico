Algoritmo biseccion
	Leer xi,fx,xf,tol,optiontol
	Si fxi*fxf = 0 Entonces
		Escribir "Xi or xf are roots"
	Si fxi*fxf > 0 Entonces
		Escribir "Interval not valid"
			
		
	FinSi
	SiNo
	Xm=(xi + xf)/2
	Error=ABS(xm-xi)
	Mientras (Error>=tol) Y (fxm<>0) Hacer
		Si fxi*fxm<0 Entonces
			xf = xm
		SiNo
			xi = xm
		Fin Si
		xm = xi + xf /2
		Error=ABS(xm-xi)
	Fin Mientras
	Si fxm = 0 Entonces
		Escribir "Xm is a root"
	SiNo
		Escribir "Xm is a root with tol"
	Fin Si
	FinSi

FinAlgoritmo
