Algoritmo secante
	Leer fx,x1,x2,tol,optiontol,nitera
	Si x1 == 0 Entonces
		Escribir "X1 is a root"
	Si x2 ==0 Entonces
		Escribir "X2 is a root"
	Fin Si
	SiNo
		error = tol+1.0
		ite = 0
		fx1=x1
		fx2 = x2
		Mientras error>=tol Y ite < nitera Hacer
			Si fx2-fx1==0 Entonces
				Escribir "Indefinition, divided by 0(fx-fx-1=0)"
			
				xm = x2
				x2=x2-(fx2*x2-x1)/(fx2-fx1)
				x1 = xm
			Fin Si
			Si optiontol Entonces
				error=ABS(x2-x1)
			SiNo
				error=ABS(x2-x1)/x2
			Fin Si
			fx1 = x1
			fx2 = x2
		Fin Mientras
		Si error<tol Entonces
			Escribir "x2 is a root with tol"
		SiNo
			Escribir "we dont arrived"
		
	Fin Si	
	
FinAlgoritmo
