import sympy 
from tabulate import tabulate

def regla_falsa(xi,fx,xf,tol,optiontol):
    tabla = []
    xi = float(xi)
    xf = float(xf)
    tol = float(tol)
    if fx.subs(x,xi)*fx.subs(x,xf)==0:
        return "Xi o Xf son raiz",tabla
    elif fx.subs(x,xi)*fx.subs(x,xf)>0:
        return "Intervalo no valido"
    else:
        xm = intercepto(fx,xi,xf)
        error=tol+1.0
        if optiontol:
            error=abs(xm-xi)
        else:
            error=abs((xm-xi)/xm)
        tabla.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])
        while(error>=tol and fx.subs(x,xm)!=0):
            if fx.subs(x,xi)*fx.subs(x,xm)<0:
                xf = xm
            else:
                xi = xm
            xm = intercepto(fx,xi,xf)
            if optiontol:
                error=abs(xm-xi)
            else:
                error=abs((xm-xi)/xm)
            tabla.append([xi,round(fx.subs(x,xi),4),xm,round(fx.subs(x,xm),4),xf,round(fx.subs(x,xf),4),error])
        if fx.subs(x,xm)==0:
            return "Xm es raiz",tabla
        else:
            return "Xm es una raiz con tolerancia",tabla
def intercepto(fx,xi,xf):
    m=(fx.subs(x,xf)-fx.subs(x,xi))/(xf-xi)
    medio=xi-(fx.subs(x,xi)/m)
    return medio
#Main
x = sympy.Symbol('x')                                               #Definimos una funcion con Sympy
fdx = x**3-7.51*x**2+18.4239*x-14.8331
resultado=regla_falsa(3,fdx,3.5,5*10**-5,True)                                #Evaluamos la funcion
print(resultado[0])                                                 #Imprimimos el resultado con respecto a la raiz
print(tabulate(resultado[1],headers=["xi", "f(xi)", "xm","f(xm)","xf","f(xf)","error"]))




