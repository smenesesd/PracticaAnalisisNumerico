import sympy
from tabulate import tabulate
from math import e
def punto_fijo(fx,xi,tol,optiontol,gx,nitera):
    tabla = []
    xi = float(xi)
    tol = float(tol)
    if fx.subs(x,xi)==0:
        return "Xi es raiz"
    else:
        ite = 0
        error = tol+1.0
        tabla.append([ite,xi,round(gx.subs(x,xi),4),error])
        while(error>=tol and ite < nitera):
            xm = gx.subs(x,xi)
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            tabla.append([ite,xm,round(gx.subs(x,xm),4),error])
            xi = xm
        if error<tol:
            return "Xi es raiz con tolerancia",tabla
        else:
            return "No llegamos", tabla
#main
x = sympy.Symbol('x') 
gx = e**(-x)                                              
fdx = (e**(-x))-x
resultado=punto_fijo(fdx,0.5,5*10**-8,True,gx,21)                                
print(resultado[0])                                                 
print(tabulate(resultado[1],headers=["ite", "x", "g(x)","error"]))