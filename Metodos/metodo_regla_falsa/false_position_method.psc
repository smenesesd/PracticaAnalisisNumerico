Algoritmo false_position_method
	Leer xi,fx,xf,tol,optiontol
	Si xi*xf==0 Entonces
		Escribir "Xi or xf are roots"
	Si xi*xf>0 Entonces
		Escribir "Interval not valid"
	 
	Fin Si
	SiNo
		m=xf-xi/(xf-xi)
		xm=xi-(xi/m)
		error = tol+1.0
		Si optiontol Entonces
			error=ABS(xm-xi)
		SiNo
			error=ABS((xm-xi)/xm)
		Fin Si
		Mientras error>=tol Y xm <> 0 Hacer
			Si xi*xm<0 Entonces
				xf = xm
			SiNo
				xi = xm
			Fin Si
			error=ABS(xm-xi)
		Fin Mientras
		Si xm == 0 Entonces
			Escribir "xm is a root"
		SiNo
			Escribir  "Xm is a root with tol"
		Fin Si
	Fin Si

	
FinAlgoritmo
