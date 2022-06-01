from cmath import sqrt
import sympy
from sympy import var
from tabulate import tabulate
from math import e
def fixed_point(fx,xi,tol,optiontol,gx,nitera):
    table = []
    xi = float(xi)
    tol = float(tol)
    if fx.subs(x,xi)==0:
        return "Xi is a root"
    else:
        ite = 0
        error = tol+1.0
        table.append([ite,xi,round(gx.subs(x,xi),4),error])         #Añadimos la primera iteracion a la tabla
        while(error>=tol and ite < nitera):                         #En caso de no llegar a la toleracina y faltar iteraciones entramos a bucle
            xm = gx.subs(x,xi)                                      #Calculamos xm con gx
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            table.append([ite,xm,round(gx.subs(x,xm),4),error])      #Añadimos los datos de la iteracion
            xi = xm
        if error<tol:                                                #Retornamos resultado
            return "Xi is root with tol",table
        else:
            return "we don't arrived", table
#main
x = var('x')
gx = "1/((-0.4)+1.74*log(50*sqrt(x)))"                                         
fdx = "(1/x)+0.4-1.74*log(50*sqrt(x))"
f = sympy.sympify(fdx)
g = sympy.sympify(gx)
#x = sympy.Symbol('x') 
result=fixed_point(f,0.1,5*10**-8,True,g,21)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["ite", "x", "g(x)","error"]))