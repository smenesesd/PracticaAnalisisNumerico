import sympy
from tabulate import tabulate
from math import e
def newton(fx,xi,tol,optiontol,gx,nitera):
    tabla = []
    print(fx, gx)
    xi = float(xi)
    tol = float(tol)
    if fx.subs(x,xi)==0:
        return "Xi is a root"
    else:
        ite = 0
        error = tol+1.0
        tabla.append([ite,xi,round(gx.subs(x,xi),4),error])
        while(error>=tol and ite < nitera):
            if gx.subs(x,xi)==0:
                return "Indefinition, divided by 0(f'x = 0)", tabla
            xm = xi-(fx.subs(x,xi)/gx.subs(x,xi))
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            tabla.append([ite,xm,round(gx.subs(x,xm),4),error])
            xi = xm
        if error<tol:
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