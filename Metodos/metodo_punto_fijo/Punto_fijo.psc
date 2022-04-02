Algoritmo Punto_fijo
	Leer Fx, Xi, Tol, Gx, Maxite
	Si Fxi == 0 Entonces
		Escribir "En Xi hay un raiz"
	SiNo
		ite = 0
		error = Tol+1
		Mientras (error >= Tol) Y (Maxite >= ite) Hacer
			Xm = Gxi
			erro = abs(Xm-Xi)
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
