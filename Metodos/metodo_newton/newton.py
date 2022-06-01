import sympy
from tabulate import tabulate
from math import e
def newton(fx,xi,tol,optiontol,gx,nitera):
    tabla = []
    print(fx, gx)
    xi = float(xi)
    tol = float(tol)
    if fx.subs(x,xi)==0:                                        #Eavaluamos que xi sea la raiz
        return "Xi is a root"
    else:
        ite = 0
        error = tol+1.0
        tabla.append([ite,xi,round(gx.subs(x,xi),4),error])             #Añadimos la primera iteracion a tabla
        while(error>=tol and ite < nitera):                             #Mientas no lleguemos a toleracia y no superemos la iteracion
            if gx.subs(x,xi)==0:                                        #Evaluamos gx para no teener indeterminacion
                return "Indefinition, divided by 0(f'x = 0)", tabla
            xm = xi-(fx.subs(x,xi)/gx.subs(x,xi))                       #Calculamos xm con la formula de newton
            if optiontol:                                               #Calculo de error dependiendo de la opcion
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            tabla.append([ite,xm,round(gx.subs(x,xm),4),error])         #Agregamos resultados de itreacion a la tabla
            xi = xm
        if error<tol:                                                   #En caso de haber llegado por tolerancia
            return "Xi is a root with tol",tabla
        else:
            return "we don't arrived", tabla
#main
x = sympy.Symbol('x') 
gx = (-2.71**(-x))-1  
print(gx)                                           
fdx = (2.71**(-x))-x
result=newton(fdx,1,0.0001,True,gx,10)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["ite", "x", "f'(x)","error"]))