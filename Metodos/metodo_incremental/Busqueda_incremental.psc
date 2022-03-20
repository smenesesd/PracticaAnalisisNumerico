Algoritmo Busqueda_incremental
	Leer Fx,Xi,Maxite,difX
	Si Fxi == 0 Entonces
		Escribir "En Xi hay una raiz"
	SiNo
		Xf = Xi+difX
		iter = 0
		Mientras (Fxi*Fxf)>0 Y iter < Maxite Hacer
			Xi = Xf
			Xf = Xi + difX
			iter = iter+1
		Fin Mientras
		Si Fxi*Fxf == 0 Entonces
			Escribir "Xf es una raiz"
		Fin Si
		Si Fxi*Fxf < 0 Entonces
			Escribir "Entre el intervalo existe una raiz"
		SiNo
			Escribir "No es encontro una raiz en el numero de iteraciones"
		Fin Si
	Fin Si
FinAlgoritmo
