import sympy
from tabulate import tabulate
from math import e
def secant(fx,x1,x2,tol,optiontol,nitera):
    table = []
    x1 = float(x1)
    x2 = float(x2)
    tol = float(tol)
    if fx.subs(x,x1)==0:
        return "X1 is a root"
    elif fx.subs(x,x2)==0:
        return "X2 is a root"
    else:
        ite = 0
        error = tol+1.0
        fx1 = fx.subs(x,x1)
        fx2 = fx.subs(x,x2)
        table.append([ite,x1,round(fx1,4),error])
        ite += 1
        table.append([ite,x2,round(fx2,4),error])
        while(error>=tol and ite < nitera):
            if (fx2-fx1)==0:
                return "Indefinition, divided by 0(fx - fx-1 = 0)", table
            xm = x2
            x2 = x2-((fx2*(x2-x1))/(fx2-fx1))
            x1 = xm
            if optiontol:
                error=abs(x2-x1)
            else:
                error=abs((x2-x1)/x2)
            ite += 1
            fx1 = fx.subs(x,x1)
            fx2 = fx.subs(x,x2)
            table.append([ite,x2,round(fx2,14),error])
            
        if error<tol:
            return "X2 is a root with tol",table
        else:
            return "we don't arrived", table
#main
x = sympy.Symbol('x') 
gx = (-e**(-x))-1                                              
fdx = (e**(-x))-x
result=secant(fdx,1,0,0.0000001,True,10)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["ite", "x", "f(x)","error"]))