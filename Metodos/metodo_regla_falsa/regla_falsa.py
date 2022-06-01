import sympy 
from tabulate import tabulate

def false_position_method(xi,fx,xf,tol,optiontol):
    table = []
    xi = float(xi)
    xf = float(xf)
    tol = float(tol)
    if fx.subs(x,xi)*fx.subs(x,xf)==0:
        return "Xi or Xf are roots",table
    elif fx.subs(x,xi)*fx.subs(x,xf)>0:
        return "Interval not valid"
    else:
        xm = intercept(fx,xi,xf)
        error=tol+1.0
        if optiontol:
            error=abs(xm-xi)
        else:
            error=abs((xm-xi)/xm)
        table.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])
        while(error>=tol and fx.subs(x,xm)!=0):
            if fx.subs(x,xi)*fx.subs(x,xm)<0:
                xf = xm
            else:
                xi = xm
            xm = intercept(fx,xi,xf)
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            table.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])
        if fx.subs(x,xm)==0:
            return "Xm is a root ",table
        else:
            return "Xm is a root with tol ",table
def intercept(fx,xi,xf):
    m=(fx.subs(x,xf)-fx.subs(x,xi))/(xf-xi)
    medio=xi-(fx.subs(x,xi)/m)
    return medio
#Main
x = sympy.Symbol('x')                                               
fdx = x**3-7.51*x**2+18.4239*x-14.8331
result=false_position_method(3,fdx,3.5,0.0001,True)                                
print(result[0])                                                 
print(tabulate(result[1],headers=["xi", "f(xi)", "xm","f(xm)","xf","f(xf)","error"]))




