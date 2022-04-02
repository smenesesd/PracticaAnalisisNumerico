import sympy
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
        table.append([ite,xi,round(gx.subs(x,xi),4),error])
        while(error>=tol and ite < nitera):
            xm = gx.subs(x,xi)
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            table.append([ite,xm,round(gx.subs(x,xm),4),error])
            xi = xm
        if error<tol:
            return "Xi is root with tol",table
        else:
            return "we don't arrived", table
#main
x = sympy.Symbol('x') 
gx = e**(-x)                                              
fdx = (e**(-x))-x
result=fixed_point(fdx,0.5,5*10**-8,True,gx,21)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["ite", "x", "g(x)","error"]))