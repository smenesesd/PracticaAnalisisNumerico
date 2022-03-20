import sympy 
from tabulate import tabulate

def incremental(fx, xi, maxite, difx):
    xi = float(xi)
    difx = float(difx)
    tabla = []                                                      #Inicializamos la tabla para almacenar los datos de cada iteracion              
    if fx.subs(x, xi)==0:                                           #En caso de que F(xi) sea raiz
        return "xi si es raiz",tabla
    else:                                                           #definimos xf y agregamos los primeros datos a la tabla
        xf = xi + difx
        ite = 0
        tabla.append([ite,xi,round(fx.subs(x, xi),4)])
    #Ciclo para realizar las iteraciones mientras se cumpla que no hay una raiz o superamos el maximo de iteraciones
        while(fx.subs(x, xi)*fx.subs(x, xf)>0)and (ite<maxite):
            xi = xf
            xf = xi + difx
            ite += 1
            tabla.append([ite,xi,round(fx.subs(x, xi),4)])          #Agregamos cada iteracion a al tabla
        tabla.append([ite+1,xf,round(fx.subs(x, xf),4)])            #Agremamos el xf a la tabla
        if fx.subs(x, xi)*fx.subs(x, xf)==0:                        #Si F(xi)*F(xf)==0 entonces tenemos una raiz en xf
            return "xf es raiz",tabla
        elif fx.subs(x, xi)*fx.subs(x, xf)<0:                       #Si existe un cambio de signo enotnces hay una raiz en ese intervalo
            return "Entre ellos hay raiz",tabla
        else:                                                       #Sino, no tenemos raiz en ese numero de iteraciones
            return "No encontre raiz en el maximo de iteraciones",tabla

#Main
x = sympy.Symbol('x')                                               #Definimos una funcion con Sympy
fdx = x**3-7.51*x**2+18.4239*x-14.8331
resultado=incremental(fdx,0,250,0.1)                                #Evaluamos la funcion
print(resultado[0])                                                 #Imprimimos el resultado con respecto a la raiz
print(tabulate(resultado[1],headers=["Iteracion", "x", "F(x)"]))    #Imprimimos la tabla con las iteraciones
            
