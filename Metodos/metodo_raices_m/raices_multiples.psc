Algoritmo raices_multiples
	Escribir Fx, Xi, d1Fx, d2Fx, Tol, Maxite
	Si Fxi == 0 Entonces
		Escribir "Xi es raiz"
	SiNo
		ite = 0
		error = Tol + 1
		Mientras (error >= tol) Y (ite < Maxite) Hacer
			Xm = Xi -((Fxi-dFxi)/((dFxi^2)-(Fxi*d2Fxi)))
			error = abs(Xm - Xi)
			ite = ite + 1
			Xi = Xm
		Fin Mientras
		Si error <= Tol Entonces
			Escribir "Xi es raiz con tol"
		SiNo
			Escribir "No se encontro una raiz en el numero de iteraciones"
		Fin Si
	Fin Si
FinAlgoritmo
