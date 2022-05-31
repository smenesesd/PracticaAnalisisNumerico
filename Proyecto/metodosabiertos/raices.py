import sympy
from tabulate import tabulate
from sympy import var
from math import e
def root_m(fx,xi,fx1,fx2,tol,optiontol,nitera):
    x = var('x')
    fx = sympy.sympify(fx)
    fx1 = sympy.sympify(fx1)
    fx2 = sympy.sympify(fx2)
    table = [["ite", "x", "f(x)","f'(x)","f''(x)","error"]]
    xi = float(xi)
    tol = float(tol)
    if fx.subs(x,xi)==0:
        return "Xi is a root"
    else:
        ite = 0
        error = tol+1.0
        result_fx = fx.subs(x,xi)
        result_fx1 = fx1.subs(x,xi)
        result_fx2 = fx2.subs(x,xi)
        table.append([ite,xi,round(result_fx,4),round(result_fx1,4),round(result_fx2,4),error])
        while(error>=tol and ite < nitera):
            xm = xi-((result_fx*result_fx1)/((result_fx1**2)-(result_fx*result_fx2)))
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            ite += 1
            xi = xm
            result_fx = fx.subs(x,xi)
            result_fx1 = fx1.subs(x,xi)
            result_fx2 = fx2.subs(x,xi)
            table.append([ite,xi,round(result_fx,14),round(result_fx1,14),round(result_fx2,14),error])
        if error<tol:
            return "X1 is a root with tol",table
        else:
            return "we don't arrived", table
#main
#x = sympy.Symbol('x') 
#fdx1 = x*e**(x) 
#fdx2 = x*e**(x)+e**(x)                                            
#fdx = x*e**(x)-e**(x)+1

#result=root_m(fdx,0.5,fdx1,fdx2,0,True,10)                                
#print(result[0])                                                 
#print(tabulate(result[1],headers=["ite", "x", "f(x)","f'(x)","f''(x)","error"]))
